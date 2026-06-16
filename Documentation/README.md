**# Surveillance // Input Capture Monitor**



An educational security utility designed to demonstrate the mechanics of keyboard event listening and local data exfiltration. This tool provides insight into how 'spyware' and 'infostealers' monitor user input at the kernel/OS level.



**## Project Structure**

```text

keylogger-edu/

├── app.py                # Capture Engine (pynput Listener)

├── keylog.txt            # Local Exfiltration File

├── requirements.txt      # Dependencies

├── static/

│   ├── css/style.css     # Digital Surveillance UI

│   └── js/main.js        # Real-time Polling \& UI Handlers

└── templates/

&nbsp;   └── index.html        # Monitoring Dashboard



**Technical Implementation**

* **Input Hooking**: Utilizes the pynput library to create a global listener for keyboard events, capturing both alphanumeric characters and special system keys.
* **Multi-Threading**: Runs the capture engine in a background thread while maintaining a responsive Flask UI for data review.
* **Real-Time Exfiltration**: Logs keystrokes to a local flat-file (keylog.txt) which is polled every 1000ms by the frontend via a REST API.
* **Data Parsing**: Distinguishes between standard character input and system-level keys (e.g., Space, Enter, Backspace) to provide a readable context for the captured stream.



**Setup \& Execution**

Initialize Engine:



├── python app.py

&nbsp;	├── *The system operates on Port 5008.*



Conduct Monitoring:

* Open any other application (Notepad, Browser, etc.).
* Type information into the external window.
* Return to the Dashboard to see the intercepted data appear in the capture stream.



**Building the Portable Monitor**

Windows Command: pyinstaller --onefile --noconsole --add-data "templates;templates" --add-data "static;static" app.py



**Security Disclaimer \& Insight**

This tool is for Educational Use Only. Running this script demonstrates why modern operating systems and Antivirus (AV) software provide warnings when a program attempts to 'hook' into input devices. This is a primary behavior of unauthorized information collection tools.

