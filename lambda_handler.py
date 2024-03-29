import json
import os

# pip3 install and zip to lambda
import requests

def lambda_handler(event, context):
      #  Get the event json object
      # Extract the html to issue from github webhook
      # Create a new connection to "SLACK_URL"
      # send response to the connection
      slack_url = os.environ['SLACK_URL']

      # {
#    "action": "opened",
#    "issue": {
#      "url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
#      "number": 1347,
#      ...
#    },
# issue.url