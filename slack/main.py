import slack
import json
import base64


def notify_slack(data, context):
    BOT_ACCESS_TOKEN = "xoxb-1236111082277-1290825432211-5h6UuRb7u23ZDfJWqBwLp6WL"
    CHANNEL_ID = "C018BRVC146"

    slack_client = slack.SlackClient(BOT_ACCESS_TOKEN)

    # pubsub_message = data

    # notification_data = base64.b64decode(data["data"]).decode("utf-8")
    # notification_data = json.loads(notification_data)
    # budget_notification_text = "予算額：{0} ({1})\n利用料金：{2} ({1})\n利用開始日時：{3}".format(
    #     notification_data.get("budgetAmount"),
    #     notification_data.get("currencyCode"),
    #     notification_data.get("costAmount"),
    #     notification_data.get("costIntervalStart"),
    # )

    try:
        slack_client.api_call(
            # "chat.postMessage", channel=CHANNEL_ID, text=budget_notification_text
            "chat.postMessage",
            channel=CHANNEL_ID,
            text="testです",
        )

        print("done")
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
