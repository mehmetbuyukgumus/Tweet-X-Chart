from openai import OpenAI
from dotenv import load_dotenv
from src.parsing import parsing_tweets
from src.tweets import get_tweets
import os
import json

load_dotenv()

async def tweet_generator(username):
    try:
        data = await get_tweets(username) 
    except Exception as e:
        print(f"Hesap kitli {e}")
        return None
    try:
        tweets = parsing_tweets(data)
    except Exception as e:
        print(f"Hesap kitli {e}")
        return None    
    client = OpenAI(api_key=os.getenv("api_key"))
    response = client.chat.completions.create(
        model="gpt-4-1106-vision-preview",
        messages=[
            {"role": "system", "content": os.getenv("content_system")},
            {"role": "user", "content": tweets}
        ]
    )
    if response.choices:
        content = response.choices[0].message.content
        return content
    else:
        print("No response")
        return None
