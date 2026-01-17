# StudyResourceHelper

A Python-based utility bot designed to assist educational communities like r/JEENEETards and r/BTechtards.

## 🚀 Features
* **Real-time Monitoring:** Uses PRAW `stream.submissions()` to watch for new posts.
* **Spam Detection:** filters posts containing known spam keywords.
* **Link Safety:** Basic validation to ensure shared resources do not link to malicious domains.
* **Local Caching:** Uses `sqlite3` to prevent processing the same post twice.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Library:** PRAW (Python Reddit API Wrapper)
* **Database:** SQLite (Local)

## 📦 Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Configure `client_id` and `client_secret` in `main.py`.
4. Run the bot: `python main.py`

*Note: This project is currently in Alpha and is pending Reddit API approval.*