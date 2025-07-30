import os
import urllib.request
import socket
import time

# URL list can also be loaded from a remote file or manually listed here
file_urls = [
    "https://cdn.jsdelivr.net/gh/rottentomatochesecake/dsa@main/file.txt",
    "https://cdn.jsdelivr.net/gh/rottentomatochesecake/dsa@main/file.txt",
]

# Folder to save files
download_dir = os.path.expanduser("~/downloads_from_server")
os.makedirs(download_dir, exist_ok=True)

# Check internet connection
def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

# Download files
def download_files():
    for url in file_urls:
        filename = os.path.basename(url)
        filepath = os.path.join(download_dir, filename)

        if not os.path.exists(filepath):
            try:
                print(f"Downloading: {filename}")
                urllib.request.urlretrieve(url, filepath)
                print(f"Saved: {filepath}")
            except Exception as e:
                print(f"Error downloading {filename}: {e}")
        else:
            print(f"Already downloaded: {filename}")

# Daemon loop
def main():
    print("Daemon started. Waiting for internet connection...")

    while True:
        if is_connected():
            print("Internet detected. Starting sync...")
            download_files()
            print("Sync complete. Sleeping for 1 hour.")
            time.sleep(3600)  # Sleep for 1 hour after successful sync
        else:
            print("No internet. Checking again in 5 minutes.")
            time.sleep(300)  # Sleep 5 mins if no connection

if __name__ == "__main__":
    main()

