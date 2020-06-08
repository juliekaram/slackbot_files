from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import json

# read in tokens
tokens = {}
with open('configs.json') as json_data:
    tokens = json.load(json_data)

# set up events adapter and client
# can also use local variables** would need to change this part of code
slack_events_adapter = SlackEventAdapter(tokens.get("slack_signing_secret"), "/slack/events")
slack_client = SlackClient(tokens.get("slack_bot_token"))

@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        send_message = "Responding to message sent by user <@%s>" % message["user"]
        slack_client.api_call("chat.postMessage", channel=channel, text=send_message)

@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

slack_events_adapter.start(port=3000)
