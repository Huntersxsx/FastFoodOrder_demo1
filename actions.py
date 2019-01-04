from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


def food_price(value):
    Price = {'薯条': 7, '汉堡': 15, '可乐': 6, '甜筒': 8, '爆米花': 10, '鸡翅': 8, '奶茶': 12, '巨无霸': 20, '套餐 A': 35, '套餐 B': 36, '套餐 C': 38}
    return Price[value]


def get_all_message(tracker):
    user_event_list = []
    user_intent_list = []
    for event in tracker.events:
        if event['event'] == 'user':
            user_event_list.append(event['parse_data']['entities'])
            user_intent_list.append(event['parse_data']['intent'].get('name'))
    return user_event_list, user_intent_list


class ActionMenu(Action):
    def name(self):
        return 'action_show_menu'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("薯条: 7元")
        dispatcher.utter_message("汉堡: 15元")
        dispatcher.utter_message("甜筒: 8元")
        dispatcher.utter_message("爆米花: 10元")
        dispatcher.utter_message("鸡翅: 8元")
        dispatcher.utter_message("奶茶: 12元")
        dispatcher.utter_message("巨无霸: 20元")
        dispatcher.utter_message("可乐: 6元")
        dispatcher.utter_message("套餐A: 35元")
        dispatcher.utter_message("套餐B: 36元")
        dispatcher.utter_message("套餐C: 38元")
        return []


class ActionAnswer(Action):
    def name(self):
        return 'action_answer'

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message.get('intent').get('name')
        if intent == 'kind_answer':
            dispatcher.utter_message("好的，请问您还需要什么吗？")
        elif intent == 'confirm':
            dispatcher.utter_message("好的，请问您还有什么需要的吗？")
        elif intent == 'deny':
            dispatcher.utter_message("好的，请稍等。")
        elif intent == 'other':
            dispatcher.utter_message("不好意思，我没能听懂您的意思，请问可以再说一遍您的需求吗？")
        return []


class ActionCalMoney(Action):
    def name(self):
        return 'action_cal_money'

    def run(self, dispatcher, tracker, domain):
        user_message, user_intent = get_all_message(tracker)
        bill = 0
        price = 0
        num = 0
        for i in range(len(user_message)):
            entities = user_message[i]
            price_list = []
            num_list = []
            if (user_intent[i] == 'kind_answer' or 'confirm') and (entities != []):
                for x in entities:
                    if x.get("entity") == "food":
                        value01 = x.get("value")
                        price_tmp = food_price(value01)
                        price_list.append(price_tmp)
                    elif x.get("entity") == "quan":
                        value02 = x.get("value")
                        num_tmp = int(value02)
                        num_list.append(num_tmp)
                bill_list = [price_list[i] * num_list[i] for i in range(len(price_list))]
                bill_tmp = sum(bill_list)
                bill += bill_tmp
        dispatcher.utter_message("您好，一共是{}元。".format(bill))
        #dispatcher.utter_message("user_message:{}".format(user_message))
        #dispatcher.utter_message("user_intent:{}".format(user_intent))
        #dispatcher.utter_message("entities:{}".format(user_message[1]))
        #dispatcher.utter_message("length:{}".format(len(user_message)))
        #dispatcher.utter_message("entity:{}".format(user_message[1][0].get("value")))
        return []

#entities
'''
entities:[{'start': 2, 'end': 4, 'value': '1', 'entity': 'quan', 'confidence': 0.9880497969162052, 'extractor': 'ner_crf', 'processors': ['ner_synonyms']},
 {'start': 4, 'end': 6, 'value': '汉堡', 'entity': 'food', 'confidence': 0.9927043923488859, 'extractor': 'ner_crf'},
  {'start': 7, 'end': 9, 'value': '1', 'entity': 'quan', 'confidence': 0.9980485915344901, 'extractor': 'ner_crf', 'processors': ['ner_synonyms']}, 
  {'start': 9, 'end': 11, 'value': '可乐', 'entity': 'food', 'confidence': 0.9982513564658912, 'extractor': 'ner_crf'}, 
  {'start': 12, 'end': 14, 'value': '1', 'entity': 'quan', 'confidence': 0.9972201526590433, 'extractor': 'ner_crf', 'processors': ['ner_synonyms']}, 
  {'start': 14, 'end': 16, 'value': '鸡翅', 'entity': 'food', 'confidence': 0.9978083810312598, 'extractor': 'ner_crf'}]
'''









