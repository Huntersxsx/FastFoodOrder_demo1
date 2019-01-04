## Say Bye
* goodbye
  - utter_goodbye

## Story order1
* greet
    - utter_greet
    - utter_help
* order_meal
    - utter_ask_kind
    - action_show_menu
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* deny
    - action_answer
    - action_cal_money
    - utter_wait
    - utter_bless

## Story order2
* greet
    - utter_greet
    - utter_help
* order_meal
    - utter_ask_kind
    - action_show_menu
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* deny
    - action_answer
    - action_cal_money
    - utter_wait
    - utter_bless

## Story order3
* greet
    - utter_greet
    - utter_help
* order_meal
    - utter_ask_kind
    - action_show_menu
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* deny
    - action_answer
    - action_cal_money
    - utter_wait
    - utter_bless


## Story order4
* greet
    - utter_greet
    - utter_help
* order_meal
    - utter_ask_kind
    - action_show_menu
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"] "quan": ["1","2"]}
    - action_answer
* deny
    - action_answer
    - action_cal_money
    - utter_wait
    - utter_bless
    
## Story 2 times
* greet
    - utter_greet
    - utter_help
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* deny
    - action_answer
    - action_cal_money
    - utter_wait
    - utter_bless
    
## Story 3 times
* greet
    - utter_greet
    - utter_help
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* deny
    - action_answer
    - action_cal_money
    - utter_wait
    - utter_bless
    
## Story 4 times
* greet
    - utter_greet
    - utter_help
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"] "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* deny
    - action_answer
    - action_cal_money
    - utter_wait
    - utter_bless

## Story 5 times
* greet
    - utter_greet
    - utter_help
* kind_answer{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* confirm{"food": ["可乐","汉堡","奶茶","薯条","爆米花","鸡翅","甜筒","巨无霸","套餐A","套餐B","套餐C"], "quan": ["1","2"]}
    - action_answer
* deny
    - action_answer
    - action_cal_money
    - utter_wait
    - utter_bless


