from flask import Flask
import requests
from datetime import datetime
import threading
import time

app = Flask(__name__)

def cron_job():
    while True:
        print(f"[{datetime.now()}] Running job...")
        try:
            response = requests.get("https://example.com", timeout=10)
            print(f"✅ Site is UP — Status: {response.status_code}")
        except Exception as e:
            print(f"❌ Site is DOWN — {e}")
        time.sleep(300)  # wait 5 minutes

@app.route("/")
def home():
    return f"✅ Cron Web Service is running! Last checked: {datetime.now()}"

if __name__ == "__main__":
    # Start background job thread
    t = threading.Thread(target=cron_job, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=10000)