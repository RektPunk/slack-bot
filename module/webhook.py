import requests


def send_message_slack(text: str) -> None:
    webhook_url = "https://hooks.slack.com/services/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"
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
    requests.post(webhook_url, json=payload)


if __name__ == "__main__":
    send_message_slack(text="Test")
