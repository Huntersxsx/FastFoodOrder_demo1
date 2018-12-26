from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./projects-tf/nlu/BNQ")
message = "我想听歌"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))

#python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
#python -m rasa_core.run -d models/dialogue
#python -m rasa_nlu.train -c nlu_config_tf.yml --data nlu_email.md -o models --fixed_model_name nlu --project current --verbose
#python -m rasa_core.run -d models/dialogue -u models/current/nlu

#synonym和[群组](email_item:邮箱群组)？  是不是就是value不一样：若是放在synonym群或者群组的value会变成邮箱群组，[群组](email_item:邮箱群组)的话value还是群组
#意图识别仅由intent_classifier_tensorflow_embedding决定的？和提取的实体有关吗?
#邮箱、邮箱地址都是实体，分词怎么分？实体怎么提取？
#怎么知道哪些词是jieba分不出来的？
#token_pattern，汉字、数字、字母
#有了jieba为什么还要token_pattern？


