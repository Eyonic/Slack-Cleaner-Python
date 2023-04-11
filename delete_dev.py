import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Set the API token
SLACK_TOKEN = "xoxp-"



client = WebClient(token=SLACK_TOKEN)

# Specify the channel ID and time range to delete messages
channel_id = ''

# C016CBVPCJF website-noti

oldest_time = int(time.time()) - (86400 * 7 ) # Delete messages older than 7 days

# Get the channel history
try:
    history = client.conversations_history(channel=channel_id, oldest=oldest_time)
except SlackApiError as e:
    print("Error getting channel history:", e)

# Delete each message in the history
for message in history["messages"]:
    try:
        response = client.chat_delete(channel=channel_id, ts=message["ts"])
        print("Message deleted:", response)
        time.sleep(1) # Sleep for 1 second to avoid rate limiting
    except SlackApiError as e:
        print("Error deleting message:", e)