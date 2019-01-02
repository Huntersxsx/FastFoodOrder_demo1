import re
from rasa_nlu.model import Interpreter
import pandas as pd
import numpy as np
import os


#处理测试数据的标题行
def parse_intent(line):
    match_result = re.match('^##.*:', line)   #匹配##intent:、##synonym:等
    if match_result is not None:
        headline = line[match_result.regs[0][0]:match_result.regs[0][1]]  #提取出该行的##intent:、##synonym:等
        headline = re.sub('^## *| *:$', '', headline)   #提取出intent、synonym等(即删掉## 和 :)
        content = line[match_result.regs[0][1]:]   #提取出该行中##intent:、##synonym:等后面的内容
        content = re.sub('^ +| +$', '', content)   #删掉多余的空格
        return headline, content    #返回标题的标签、标题行的内容
    return None, None


#处理测试数据的内容行
def parse_example(line):
    match_result = re.match('^-', line)   #匹配以-开头的语句
    if match_result is not None:
        example = line[match_result.regs[0][1]:]   #提取出-后面的内容,即样例
        entities = re.findall('\[[^\[]*\)', example)  #找到该行所有[value](entity)
        entities = ','.join(entities)    #转变成字符串
        sentence = re.sub('\([^\(\)]*.\)|\[|\]|^ +| +$', '', example)  #删除开头和结尾的空格、[、]、()及其里面的内容
        return sentence, entities      #返回测试样例语句、实体信息
    return None, None


#处理测试数据文件
def parse_file(file_path, intent_list, example_list, entity_list):
    current_intent = None
    current_headline_name = None
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as fr:
        for line in fr.readlines():   #遍历每一行
            line = line.rstrip()  # 删掉\n
            headline_name, headline_content = parse_intent(line)   #比如 intent, greet
            sentence, entities = parse_example(line)   #比如 我想再点一杯奶茶, [一杯](quan),[奶茶](food)
            if headline_name is not None:    #如果当前行是标题行，赋值
                current_intent = headline_content
                current_headline_name = headline_name
            elif sentence is not None and current_headline_name == 'intent':  #如果当前行不是标题行，且在intent标题下
                example_list.append(sentence)   #将提取出的sentence添加到example_list列表中
                entity_list.append(entities)   #将提取出的entities添加到entity_list列表中
                intent_list.append(current_intent)    #并把该语句所属的intent添加到intent_list列表中


if __name__ == '__main__':
    #对测试的原始数据进行处理
    data_dir = './nlu_data'    #测试数据的目录
    nlu_model_dir = './models/current/nlu'   #nlu训练后生产的model的目录
    output_file = './intent_pred_result.xlsx'    #结果文件
    intent_list = []   #存放intent的列表
    example_list = []  #存放样例语句的列表
    entity_list = []   #存放entiy信息的列表
    for file in os.listdir(data_dir):   #遍历测试文件夹中的所有文件
        parse_file('/'.join([data_dir, file]), intent_list, example_list, entity_list)

    #处理预测之后的数据
    pred_intent_list = []    #存放预测之后的intent的列表
    pred_conf_list = []   #存放预测的信心值的列表
    pred_entity_list = []   #存放预测之后提取的entity信息的列表
    interpreter = Interpreter.load(nlu_model_dir)   #加载interpreter
    for each in example_list:   #遍历所有的测试样例语句
        pred_result = interpreter.parse(each)   #解析该语句，得到一个字典，如{'intent': {'name': 'confirm', 'confidence': 0.959279477596283}, 'entities': [{'start': 4, 'end': 6, 'value': '1', 'entity': 'quan', 'confidence': 0.9968072253239232, 'extractor': 'ner_crf', 'processors': ['ner_synonyms']}, {'start': 6, 'end': 8, 'value': '奶茶', 'entity': 'food', 'confidence': 0.9898450748241244, 'extractor': 'ner_crf'}], 'intent_ranking': [{'name': 'confirm', 'confidence': 0.959279477596283}, {'name': 'kind_answer', 'confidence': 0.06335412710905075}, {'name': 'deny', 'confidence': 0.0219486765563488}, {'name': 'greet', 'confidence': 0.0038949400186538696}, {'name': 'goodbye', 'confidence': 0.0}, {'name': 'order_meal', 'confidence': 0.0}], 'text': '我想再点一杯奶茶'}
        pred_intent = pred_result['intent']['name']   #提取预测之后该语句的intent
        entities = pred_result['entities']   #提取预测之后该语句的所有entity信息，是个列表，列表的每个元素是字典
        entity_str_list = []
        for each in entities:
            entity_str_list.append('[' + each['value'] + '](' + each['entity'] + ')')   #将每一个entity转成[value](entity)格式的字符串，再添加到entity_str_list列表中
        entity_str = ','.join(entity_str_list)   #转成字符串，以,分割不同的entity
        pred_confidence_1 = round(float(pred_result['intent']['confidence']), 3)  # 意图分类的信心值，四舍五入到3位小数
        pred_intent_list.append(pred_intent)  
        pred_conf_list.append(pred_confidence_1)
        pred_entity_list.append(entity_str)

    # 比较数据原本的intent和预测得到的intent
    compare_result = []
    for i, each in enumerate(pred_intent_list):
        if each == intent_list[i]:
            compare_result.append(1)   #相同则记为1
        else:
            compare_result.append(0)   #不同则记为0

    # 将记录的数据按类别存放到列表中
    summary = list()
    summary.append(example_list)
    summary.append(intent_list)
    summary.append(pred_intent_list)
    summary.append(pred_conf_list)
    summary.append(compare_result)
    summary.append(entity_list)
    summary.append(pred_entity_list)

    output = np.array(summary).transpose()   #转置
    df = pd.DataFrame(output, columns=['example_input', 'Intent_from_data', 'Intent_by_pred', 'Intent_pred_conf',
                                       'IsPredIntentCorrect', 'Entity_from_data', 'Entity_by_pred'])   #每一列的标题名称
    df.to_excel(output_file, index=False)    #输出为Excel格式
    print('Done')
