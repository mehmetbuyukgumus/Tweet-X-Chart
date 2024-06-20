import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

async def get_tweets(username):
    url = "https://twitter154.p.rapidapi.com/user/tweets"

    payload = {
        "username": username,
        "include_replies": False,
        "include_pinned": False
    }
    headers = {
        "x-rapidapi-key": os.environ.get("x-rapidapi-key"),
        "x-rapidapi-host": "twitter154.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data
