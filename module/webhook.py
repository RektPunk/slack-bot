import requests
from variables.credential import WebhookUrl


def send_message_slack(text: str) -> None:
    payload = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text,
                },
            }
        ]
    }
    requests.post(WebhookUrl.SLACK_WEBHOOK_URL, json=payload)


if __name__ == "__main__":
    send_message_slack(text="Test")
