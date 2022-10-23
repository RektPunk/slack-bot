from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from variables.credential import Tokens
from variables.channel import ChannelId

app = App(token=Tokens.SLACK_BOT_TOKEN)


@app.event("team_join")
def ask_for_introduction(event, say):
    _channel_id = ChannelId.GENERAL
    _user_id = event["user"]
    _text = f"Welcome <@{_user_id}>! 🎉 You can introduce yourself in this channel."
    say(text=_text, channel=_channel_id)


@app.event("app_mention")
def greetings(event, say):
    _user_id = event["user"]
    say(f"Hello! <@{_user_id}>")


if __name__ == "__main__":
    SocketModeHandler(app, Tokens.SLACK_APP_TOKEN).start()
