import os
from dotenv import load_dotenv
from enum import Enum

try:
    load_dotenv()
except Exception as e:
    raise ("Credential load failed!")


class Tokens(str, Enum):
    SLACK_APP_TOKEN: str = os.environ["SLACK_APP_TOKEN"]
    SLACK_BOT_TOKEN: str = os.environ["SLACK_BOT_TOKEN"]

    def __repr__(self):
        return f"{self.value}"


class WebhookUrl(str, Enum):
    SLACK_WEBHOOK_URL: str = os.environ["SLACK_WEBHOOK_URL"]

    def __repr__(self):
        return f"{self.value}"
