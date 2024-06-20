# print(data["results"][19]["text"])
# print(data["results"][19]["creation_date"])
import json

def parsing_tweets(data):
    tweets = []
    for i in range(len(data["results"])):
        tweets.append(data["results"][i]["text"])
    return  tweets