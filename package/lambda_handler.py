import json
import os
import requests

def lambda_handler(event, context):
    slack_url = os.environ['SLACK_URL']
    message = {'text': 'Issue Created: ' + event["issue"]["url"]}
    response = requests.post(
        slack_url, data=json.dumps(message),
        headers={'Content-Type': 'application/json'}
    )