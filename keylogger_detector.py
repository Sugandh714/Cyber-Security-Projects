import psutil
import time
from datetime import datetime

# Define suspicious keywords
SUSPICIOUS_KEYWORDS = ['keylog', 'keyboard', 'hook', 'pynput', 'pyhook']

# Log file for suspicious activity
LOG_FILE = "suspicious_log.txt"

def is_suspicious(proc_info):
    for keyword in SUSPICIOUS_KEYWORDS:
        if any(keyword in str(value).lower() for value in proc_info.values()):
            return True
    return False

def scan_processes():
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            if is_suspicious(proc.info):
                alert_user(proc.info)
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue

def alert_user(proc_info):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] SUSPICIOUS PROCESS DETECTED:\n{proc_info}\n\n"
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(message)

# --- Main loop for real-time detection ---
print("🔍 Keylogger Detector Running... Press Ctrl+C to stop.\n")

try:
    while True:
        scan_processes()
        time.sleep(10)  # check every 10 seconds
except KeyboardInterrupt:
    print("\n❌ Detector stopped by user.")
