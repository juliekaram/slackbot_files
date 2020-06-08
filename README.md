# slackbot_events_api_example
Basic example of how to build a slack bot using the events API.

## Main Features
1. Reply to certain message when it is posted to a slack channel with the bots handle mentioned.

## Explanation of Files
1. slackbot_events_api_example.py: Source code for the slack bot.
2. configs.json: Configuration file.  

## How to Configure the slackbot_events_api_example
In order for this slack bot to work it will need a few keys to authenticate to slack, the contents of the config file as well as what they are can be found below. 
```json
{
  "slack_bot_token":"",
  "slack_signing_secret":""
}
```

1. slack_bot_token: This is the token of the bot user configured in slack
2. slack_signing_secret: This is the signing secret that the bot will use to authenticate to the channel sent by the events subscription.

## ** can also store in local environment
Would need to do something like...
In terminal:
    export SLACK_API_TOKEN="..."
    export SLACK_SIGNING_SECRET="..."

In python file:
call values by using... os.environ['SLACK_API_TOKEN']/ os.environ['SLACK_SIGNING_SECRET']

## How to Run
1. Create an application in slack
2. Enable OAuth for the bot
3. Grant the bot user scopes (need char:write:bot, message.channels)
4. Enable event subscriptions
5. Copy the slack bot token and the slack signing secret to the configs.json file
6. In terminal session a, launch ngrok
7. In terminal session b, launch the slack bot
    ```bash
    pip3 install -r requirements.txt
    python3 slackbot_events_api_example.py
    ```
8. Now you should be able to go to the slack app, invite the bot and then send a message
9. If everything went correctly, bot will respond

