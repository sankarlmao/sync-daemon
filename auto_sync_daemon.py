import time
import urllib.request

URL = "https://cdn.jsdelivr.net/gh/rottentomatochesecake/dsa@main/file.txt"
DEST_FILE = "/home/YOUR_USERNAME/sync_log.txt"  # <-- Change this!

def is_connected():
    try:
        urllib.request.urlopen("https://www.google.com", timeout=5)
        return True
    except:
        return False

def download_and_log():
    try:
        with urllib.request.urlopen(URL) as response:
            content = response.read().decode("utf-8")
            with open(DEST_FILE, "w") as f:
                f.write(content)
    except Exception as e:
        pass  # Fail silently

while True:
    if is_connected():
        download_and_log()
    time.sleep(300)  # 5 minutes
