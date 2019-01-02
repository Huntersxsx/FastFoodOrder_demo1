from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")
message = "我想要一杯可乐"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))

#训练NLU：  python -m rasa_nlu.train -c nlu_config_tf.yml --data data/nlu_data/ -o models --fixed_model_name nlu --project current --verbose
#训练Core： python -m rasa_core.train -d domain.yml -s data/stories_order.md -o models/dialogue
#运行对话： python -m rasa_core.run -d models/dialogue -u models/current/nlu
#自定义Action： python -m rasa_core_sdk.endpoint --actions actions
#加上endpoint后运行对话： python -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml
#interative training： python -m rasa_core.train interactive -o models/dialogue -d domain.yml -s data/stories_order.md --nlu models/current/nlu --endpoints endpoints.yml
#旧版本interative training： python -m rasa_core.train online -o models/dialogue -d domain.yml -s data/stories_order.md --nlu models/current/nlu --endpoints endpoints.yml
# Debug模式： python -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml --debug
#可视化流程(新版本有)： localhost:5005/visualization.html

