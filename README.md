# Slack-Cleaner-Python

Introduction:
This Python script uses the Slack API to delete messages from a specific Slack channel that are older than 7 days. It takes advantage of the WebClient and SlackApiError modules from the Slack SDK to access the Slack workspace and perform the message deletion.

Code Explanation:

The first step is to import the required modules. The 'os' module is imported to access operating system functionalities, and the 'time' module is used to add a delay of 1 second between message deletions to avoid rate limiting. The 'WebClient' and 'SlackApiError' modules are imported from the Slack SDK to interact with the Slack workspace.

The Slack API token is set to a constant value 'SLACK_TOKEN', which is used to initialize the WebClient.

The channel ID to delete messages from is specified in the 'channel_id' variable, and the time range for deleting messages is set to 7 days using the 'oldest_time' variable.

The 'client.conversations_history' method is used to get the history of the specified channel, using the 'channel_id' and 'oldest_time' variables as parameters. If an error occurs while retrieving the channel history, it is caught using the 'SlackApiError' module and printed to the console.

The script loops through each message in the channel history and deletes it using the 'client.chat_delete' method. The message timestamp 'ts' is passed as a parameter to the method to specify which message to delete. A delay of 1 second is added between each deletion using the 'time.sleep' method to avoid rate limiting. If an error occurs while deleting a message, it is caught using the 'SlackApiError' module and printed to the console.

The script prints a message to the console for each message successfully deleted.

Usage:

Replace the 'SLACK_TOKEN' constant with a valid Slack API token.

Set the 'channel_id' variable to the ID of the Slack channel you want to delete messages from.

Run the Python script.

Note:
Make sure the Slack API token has the necessary permissions to access and delete messages from the specified Slack channel. The user associated with the token must also be a member of the channel.

<a href="https://www.buymeacoffee.com/Eyonic" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
