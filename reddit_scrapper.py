import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def scrape_user_content(username, limit=50):
    user = reddit.redditor(username)
    user_data = []

    try:
        for comment in user.comments.new(limit=limit):
            user_data.append({
                "type": "comment",
                "text": comment.body,
                "subreddit": str(comment.subreddit),
                "permalink": f"https://reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"⚠️ Failed to fetch comments: {e}")

    try:
        for submission in user.submissions.new(limit=limit):
            user_data.append({
                "type": "post",
                "text": submission.title + "\n\n" + submission.selftext,
                "subreddit": str(submission.subreddit),
                "permalink": f"https://reddit.com{submission.permalink}"
            })
    except Exception as e:
        print(f"⚠️ Failed to fetch posts: {e}")

    return user_data
