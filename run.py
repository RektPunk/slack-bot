from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from variables.credential import Tokens
from variables.channel import ChannelId

app = App(token=Tokens.SLACK_BOT_TOKEN)


@app.event("app_mention")
def greetings(event, client, message, say):
    print("event:", event)
    print("client:", client)
    print("message:", message)
    say(f'hello! <@{event["user"]}>')


if __name__ == "__main__":
    SocketModeHandler(app, Tokens.SLACK_APP_TOKEN).start()
