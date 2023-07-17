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
        if datetime.fromtimestamp(comment.created_utc) < cutoff_time and comment.score < 1:
            if random.random() < 0.95:
                comment.delete()
                # add comment to log with timestamp, score, and body
                deleted_comments_log[comment.id] = {
                    'timestamp': comment.created_utc,
                    'score': comment.score,
                    'body': comment.body
                }
    
    # return log of deleted comments
    return {
        'statusCode': 200,
        'body': deleted_comments_log
    }
           
