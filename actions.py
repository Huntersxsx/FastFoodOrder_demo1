from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


def food_price(value):
    Price = {'薯条': 7, '汉堡': 15, '可乐': 6, '甜筒': 8, '爆米花': 10, '鸡翅': 8, '奶茶': 12}
    return Price[value]


def get_all_message(tracker):
    user_event_list = []
    for event in tracker.events:
        if event['event'] == 'user':
            user_event_list.append(event['parse_data']['entities'])
    return user_event_list


class ActionCalMoney(Action):
    def name(self):
        return 'action_cal_money'

    def run(self, dispatcher, tracker, domain):
        user_message = get_all_message(tracker)
        bill = 0
        price = 0
        num = 0
        for i in range(len(user_message)):
            entities = user_message[i]
            for x in entities:
                if x.get("entity") == "food":
                    value = x.get("value")
                    price = food_price(value)
                elif x.get("entity") == "quan":
                    value = x.get("value")
                    num = int(value)
            bill += price * num
        dispatcher.utter_message("您好，一共是{}元。".format(bill))
        #dispatcher.utter_message("entities:{}".format(user_message[1]))
        #dispatcher.utter_message("length:{}".format(len(user_message)))
        #dispatcher.utter_message("entity:{}".format(user_message[1][0].get("value")))
        return []









