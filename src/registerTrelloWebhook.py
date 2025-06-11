# One-Time Use! Register the webhook
import requests
import json
from config import Config

config = Config()

payload = {
    "description": "Gaming Through Time Webhook",
    "callbackURL": config.TRELLO_WEBHOOK_CALLBACK,
    "idModel": config.TRELLO_BOARD_ID_GAMING,
    "secret": config.TRELLO_WEBHOOK_SECRET,
    "key": config.TRELLO_API_KEY,
    "token": config.TRELLO_API_TOKEN
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    config.TRELLO_API_ENDPOINT,
    headers=headers,
    data=json.dumps(payload)
)

if response.ok:
    print("Webhook registered!")
    print(json.dumps(response.json(), indent=2))
else:
    print("Failed to register webhook")
    print(response.status_code, response.text)
