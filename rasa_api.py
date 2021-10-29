# from rasa import api,model
# from rasa import __main__ as ma
# from rasa_sdk import Tracker
# from rasa import core
# import actions.actions as action
import requests

# PARSE = "http://localhost:5005/model/parse"
URL = "http://localhost:5005/webhooks/rest/webhook"
# ADD_MESSAGE = ""
# PARAMS = {"text":"hello"} # user_input should be in dictionary form

def main(userIn):
    message = {"sender":"test_user", "message": userIn}
    response = requests.post(url=URL, json=message)
    # tracker = core.retrieve()

    # intent = action.ActionPrintIntent()

    # print('Your intent is ', intent)
    data = response.json()
    userID = data[0]['recipient_id']
    # print('-----------',userID)
    for i in data:
        # print(i.keys())
        if i['recipient_id'] == userID:
            if 'text' in i:
                print(i['text'])
            if 'image' in i:
                print(i['image'])



main("hello")