import re
from rasa_nlu.model import Interpreter
import pandas as pd
import numpy as np
import os


def parse_intent(line):
    match_result = re.match('^##.*:', line)   #匹配##intent:、##synonym:等
    if match_result is not None:
        headline = line[match_result.regs[0][0]:match_result.regs[0][1]]  #提取出该行的##intent:、##synonym:等
        headline = re.sub('^## *| *:$', '', headline)   #提取出intent、synonym等(即删掉## 和 :)
        content = line[match_result.regs[0][1]:]   #提取出该行中##intent:、##synonym:等后面的内容
        content = re.sub('^ +| +$', '', content)   #删掉多余的空格
        return headline, content
    return None, None


def parse_example(line):
    match_result = re.match('^-', line)   #匹配以-开头的语句
    if match_result is not None:
        example = line[match_result.regs[0][1]:]   #提取出-后面的内容,即样例
        entities = re.findall('\[[^\[]*\)', example)  #找到该行所有[value](entity)
        entities = ','.join(entities)    #转变成字符串
        sentence = re.sub('\([^\(\)]*.\)|\[|\]|^ +| +$', '', example)  #删除开头和结尾的空格、[、]、()及其里面的内容
        return sentence, entities
    return None, None


def parse_file(file_path, intent_list, example_list, entity_list):
    current_intent = None
    current_headline_name = None
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as fr:
        for line in fr.readlines():
            line = line.rstrip()  # 删掉\n
            headline_name, headline_content = parse_intent(line)   #比如 intent, greet
            sentence, entities = parse_example(line)   #z
            if headline_name is not None:
                current_intent = headline_content
                current_headline_name = headline_name
            elif sentence is not None and current_headline_name == 'intent':
                example_list.append(sentence)
                entity_list.append(entities)
                intent_list.append(current_intent)


if __name__ == '__main__':
    # load input nlu training data
    data_dir = './nlu_data'    #测试数据的目录
    nlu_model_dir = './models/current/nlu'   #训练数据的目录
    output_file = './intent_pred_result.xlsx'    #结果文件
    intent_list = []
    example_list = []
    entity_list = []
    for file in os.listdir(data_dir):
        parse_file('/'.join([data_dir, file]), intent_list, example_list, entity_list)

    # nlu model prediction
    pred_intent_list = []
    pred_conf_list = []
    pred_entity_list = []
    interpreter = Interpreter.load(nlu_model_dir)
    # interpreter = Interpreter.load('../tmp/nlu/BNQ')
    for each in example_list:
        pred_result = interpreter.parse(each)
        pred_intent = pred_result['intent']['name']
        entities = pred_result['entities']
        entity_str_list = []
        for each in entities:
            entity_str_list.append('[' + each['value'] + '](' + each['entity'] + ')')
        entity_str = ','.join(entity_str_list)
        pred_confidence_1 = round(float(pred_result['intent']['confidence']), 3)  # save value to 3 decimal position
        pred_intent_list.append(pred_intent)
        pred_conf_list.append(pred_confidence_1)
        pred_entity_list.append(entity_str)

    # compare prediction and ground truth
    compare_result = []
    for i, each in enumerate(pred_intent_list):
        if each == intent_list[i]:
            compare_result.append(1)
        else:
            compare_result.append(0)

    # output
    summary = list()
    summary.append(example_list)
    summary.append(intent_list)
    summary.append(pred_intent_list)
    summary.append(pred_conf_list)
    summary.append(compare_result)
    summary.append(entity_list)
    summary.append(pred_entity_list)

    output = np.array(summary).transpose()
    df = pd.DataFrame(output, columns=['example_input', 'Intent_from_data', 'Intent_by_pred', 'Intent_pred_conf',
                                       'IsPredIntentCorrect', 'Entity_from_data', 'Entity_by_pred'])
    df.to_excel(output_file, index=False)
    print('Done')
