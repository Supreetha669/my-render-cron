import requests
from datetime import datetime

def run():
    print(f"[{datetime.now()}] Cron job started!")
    
    url = "https://example.com"
    try:
        response = requests.get(url, timeout=10)
        print(f"✅ {url} is UP — Status: {response.status_code}")
    except Exception as e:
        print(f"❌ {url} is DOWN — Error: {e}")
    
    print("✅ Job complete.")

if __name__ == "__main__":
    run()
