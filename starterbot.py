# send message through slackbot using webhook

import requests
import json
import os

# create data type that you want to send... example is simple text..
data = {
    "text": "hi this is sample bot" # message inside can be changed
}

# webhook from app will be used to connect to slack... need to export to environment before
# running this file

# type webhook_slack='webhook...' in terminal
webhook = os.environ.get("webhook_slack")
requests.post(webhook, json.dumps(data))

# note: the webhook is specific to the channel that the bot is invited to;
# message will be posted to that channel






