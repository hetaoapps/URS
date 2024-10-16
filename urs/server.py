import os
from flask import Flask, jsonify, request
import subprocess  # Import the subprocess module
import argparse
from argparse import Namespace
from dotenv import load_dotenv
from urs.utils.Tools_api import RunApi
import praw


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/subreddit')
def subreddit():
    r = request.args.get('r', "")
    c = request.args.get('c', "h")
    n = request.args.get('n', "10")

    subreddit = [[r, c, n]]

    if r == "":
        return jsonify({"error": "no subreddit provided."})

    namespace = Namespace(
        subreddit=subreddit,
        redditor=None,
        comments=None,
        basic=False,
        rules=False,
        raw=False,
        live_subreddit=None,
        live_redditor=None,
        stream_submissions=False,
        frequencies=None,
        wordcloud=None,
        y=True,
        nosave=False,
        csv=False
    )
    load_dotenv()

    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
    )

    res = RunApi(namespace, reddit).run_urs()
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
