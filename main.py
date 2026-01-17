import praw
import time
import logging
import sqlite3
import re
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StudyResourceBot:
    def __init__(self):
        # Initialize PRAW with placeholder credentials
        # Ideally, these would be environment variables in a production app
        self.reddit = praw.Reddit(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
            user_agent="StudyResourceHelper/0.1 by YourUsername"
        )
        self.subreddit_name = "JEENEETards+BTechtards"
        self.db_connection = sqlite3.connect("bot_cache.db")
        self._setup_db()

    def _setup_db(self):
        """Sets up a local SQLite cache for duplicate detection."""
        cursor = self.db_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS seen_posts (
                id TEXT PRIMARY KEY,
                title TEXT,
                timestamp DATETIME
            )
        ''')
        self.db_connection.commit()

    def check_spam_keywords(self, text):
        """Simple filter to detect low-quality keywords."""
        spam_keywords = ["buy now", "click here", "free bitcoin", "urgent help needed"]
        return any(keyword in text.lower() for keyword in spam_keywords)

    def validate_links(self, text):
        """Checks for malicious domains in text (Mock implementation)."""
        # In a real scenario, this would check against a blacklist API
        urls = re.findall(r'(https?://\S+)', text)
        for url in urls:
            if "malicious-site.com" in url:
                return False
        return True

    def run(self):
        """Main loop to monitor submissions."""
        logging.info(f"Starting bot monitoring on {self.subreddit_name}...")
        subreddit = self.reddit.subreddit(self.subreddit_name)

        try:
            for submission in subreddit.stream.submissions(skip_existing=True):
                # 1. Check for duplicates (Mock logic)
                # 2. Analyze content for keywords
                # 3. Log helpful resources
                
                if self.check_spam_keywords(submission.title):
                    logging.warning(f"Potential spam detected: {submission.id}")
                    continue
                
                if not self.validate_links(submission.selftext):
                    logging.warning(f"Unsafe link detected in: {submission.id}")
                    continue

                logging.info(f"Processed valid submission: {submission.title[:30]}...")
                
                # Respect API rate limits strictly
                time.sleep(2) 

        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            time.sleep(60) # Backoff on error

if __name__ == "__main__":
    bot = StudyResourceBot()
    bot.run()