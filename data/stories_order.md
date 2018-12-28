## Say Bye
* goodbye
  - utter_goodbye

## Story 1
* greet
    - utter_greet
    - utter_help
* order_meal
    - utter_ask_kind
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒"], "quan": ["1","2"]}
    - utter_ask_again
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒"], "quan": ["1","2"]}
    - action_cal_money
    - utter_wait
    - utter_bless

## Story 2
* greet
    - utter_greet
    - utter_help
* order_meal
    - utter_ask_kind
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒"], "quan": ["1","2"]}
    - utter_ask_again
* deny
    - action_cal_money
    - utter_wait
    - utter_bless
    
## Story 3
* greet
    - utter_greet
    - utter_help
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒"], "quan": ["1","2"]}
    - utter_ask_again
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒"], "quan": ["1","2"]}
    - action_cal_money
    - utter_wait
    - utter_bless
    
## Story 4
* greet
    - utter_greet
    - utter_help
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒"], "quan": ["1","2"]}
    - utter_ask_again
* deny
    - action_cal_money
    - utter_wait
    - utter_bless


