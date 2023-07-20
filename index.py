import os
import praw
from datetime import datetime, timedelta
import random

REDDIT_APP_ID = os.getenv('REDDIT_APP_ID')
REDDIT_APP_SECRET = os.getenv('REDDIT_APP_SECRET')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')

def setup_reddit():
    reddit = praw.Reddit(
        client_id=REDDIT_APP_ID,
        client_secret=REDDIT_APP_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent="delete_comments"
    )
    return reddit

def delete_comments(reddit):
    cutoff_time_older = datetime.now() - timedelta(days=5)
    cutoff_time_newer = datetime.now() - timedelta(days=3)
    deleted_comments_log = {}

    for comment in reddit.redditor(REDDIT_USERNAME).comments.new(limit=None):
        comment_datetime = datetime.fromtimestamp(comment.created_utc)
        if cutoff_time_older < comment_datetime < cutoff_time_newer:
            if comment.score < 1 or (comment.score < 10 and random.random() < 0.50):
                comment.delete()
                deleted_comments_log[comment.id] = {
                    'timestamp': comment.created_utc,
                    'score': comment.score,
                    'body': comment.body
                }
    return deleted_comments_log

def handler(event, context):
    reddit = setup_reddit()
    deleted_comments = delete_comments(reddit) 
    print(deleted_comments)
    return deleted_comments 
