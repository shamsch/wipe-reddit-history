import os
import praw
from datetime import datetime, timedelta
import random


def handler(event, context):
    reddit = praw.Reddit(
        client_id=os.environ['REDDIT_APP_ID'],
        client_secret=os.environ['REDDIT_APP_SECRET'],
        username=os.environ['REDDIT_USERNAME'],
        password=os.environ['REDDIT_PASSWORD'],
        user_agent="delete_comments"
    )

    cutoff_time = datetime.now() - timedelta(hours=72)

    deleted_comments_log = {}

    for comment in reddit.redditor(os.environ['REDDIT_USERNAME']).comments.new(limit=None):
        if datetime.fromtimestamp(comment.created_utc) < cutoff_time:
            if comment.score < 1:
                comment.delete()
                deleted_comments_log[comment.id] = {
                    'timestamp': comment.created_utc,
                    'score': comment.score,
                    'body': comment.body
                }
            elif comment.score < 10 and random.random() < 0.50:
                comment.delete()
                deleted_comments_log[comment.id] = {
                    'timestamp': comment.created_utc,
                    'score': comment.score,
                    'body': comment.body
                }
    return {
        'statusCode': 200,
        'username': os.environ['REDDIT_USERNAME'],
        'body': deleted_comments_log,
        'execution_time': f'UTC time: {datetime.now()}'
    }
