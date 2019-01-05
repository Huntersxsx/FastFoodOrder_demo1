# FastFoodOrder

## About
This is a simple demo of a task-oriented robot, see my [blog](https://huntersxsx.github.io/2018/12/30/Rasa-bot-demo1/) for instructions.

## How to use it?
- First train the Rasa NLU model by running:

```
python -m rasa_nlu.train -c nlu_config_tf.yml --data data/nlu_data/ -o models --fixed_model_name nlu --project current --verbose
```
This will train the NLU model and store it inside the /models/current/nlu folder of your project directory.

- Then you need to train the Rasa Core model by running:

```
python -m rasa_core.train -d domain.yml -s data/stories_order.md -o models/dialogue
```

This will train the Core model and store it inside the /models/dialogue folder of your project directory.

- If you have some [custom actions](https://rasa.com/docs/core/customactions/#custom-actions), you need to run:

```
python -m rasa_core_sdk.endpoint --actions actions
```

This will start the server for emulating the custom action.

- Fianlly you need to create a new terminal TAB to run:

```
python -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml
```

This will load the assistant in your terminal for you to chat.




