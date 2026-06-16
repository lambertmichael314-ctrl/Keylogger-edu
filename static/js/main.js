const logDisplay = document.getElementById('log-display');
const clearBtn = document.getElementById('clear-btn');

// Function to refresh the logs from the server
async function refreshLogs() {
    try {
        const response = await fetch('/get_logs');
        const data = await response.json();
        
        // Update display and auto-scroll to the bottom
        logDisplay.innerText = data.logs;
        logDisplay.scrollTop = logDisplay.scrollHeight;
    } catch (err) {
        console.error("Connection to capture engine lost.");
    }
}

// Clear logs via the API
clearBtn.onclick = async () => {
    if(confirm("Confirm purge of all captured SESSION_DATA?")) {
        await fetch('/clear_logs');
        refreshLogs();
    }
};

// Update System Clock in UI
setInterval(() => {
    const now = new Date();
    document.getElementById('sys-time').innerText = now.toLocaleTimeString();
}, 1000);

// Poll for new internal keystrokes every 1 second
setInterval(refreshLogs, 1000);