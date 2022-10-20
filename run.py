from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from module.credential import Tokens


app = App(token=Tokens.SLACK_BOT_TOKEN)


@app.event("app_mention")
def who_am_i(event, client, message, say):
    print("event:", event)
    print("client:", client)
    print("message:", message)
    say(f'hello! <@{event["user"]}>')


if __name__ == "__main__":
    SocketModeHandler(app, Tokens.SLACK_APP_TOKEN).start()
