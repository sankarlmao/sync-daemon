# 📡 Auto Sync Daemon

A lightweight, user-level Python daemon that automatically downloads `.txt` files from the internet when the target PC is online. Ideal for limited-access systems, where periodic physical access is possible but internet access is unpredictable.

---

## 🔧 Features

- Runs entirely in user space — **no sudo/root required**
- Automatically checks internet connection
- Downloads `.txt` files from a list of URLs
- Avoids re-downloading existing files
- Logs all sync events
- Designed to work on Linux with Python 3

---

## 📂 Project Structure

```plaintext
.
├── auto_sync_daemon.py   # Main daemon script
├── urls.txt              # (Optional) List of file URLs to download
├── sync_log.txt          # Output log (auto-generated)
└── README.md             # This file
