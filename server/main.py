from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from src.tweet_generator import tweet_generator
import asyncio


app = Flask("__name__")
CORS(app)
api = Api(app)

class GenerateTweet(Resource):
    def get(self, username):
        tweets = asyncio.run(tweet_generator(username))
        return jsonify(tweets)
    
api.add_resource(GenerateTweet, '/api/<string:username>')

if __name__ == "__main__":
    app.run(debug=True, port=8080)
