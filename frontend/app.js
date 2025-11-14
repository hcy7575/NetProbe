/* ----------------------------
    Panel Switching
---------------------------- */
function showPanel(id) {
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    document.getElementById(id).classList.add('active');
}

/* ----------------------------
    Logging
---------------------------- */
function log(msg) {
    const box = document.getElementById('log-box');
    const time = new Date().toLocaleTimeString();
    box.textContent += `[${time}] ${msg}\n`;
    box.scrollTop = box.scrollHeight;
}

function clearLogs() {
    document.getElementById('log-box').textContent = "";
}

/* ----------------------------
    Dark Mode Toggle
---------------------------- */
function toggleDarkMode() {
    document.body.classList.toggle('dark');
}

/* ----------------------------
    Backend Status Check
---------------------------- */
async function checkBackendStatus() {
    const statusEl = document.getElementById('backend-status');
    try {
        const resp = await fetch('http://localhost:8000/');
        if (resp.ok) {
            statusEl.textContent = "Online";
            statusEl.classList.remove('status-offline');
            statusEl.classList.add('status-online');
        } else {
            statusEl.textContent = "Offline";
            statusEl.classList.remove('status-online');
            statusEl.classList.add('status-offline');
        }
    } catch (err) {
        statusEl.textContent = "Offline";
        statusEl.classList.remove('status-online');
        statusEl.classList.add('status-offline');
    }
}

// Check backend every 5 seconds
setInterval(checkBackendStatus, 5000);
checkBackendStatus();

/* ----------------------------
    SYN Flood
---------------------------- */
async function startSynFlood() {
    const target = document.getElementById('syn-target').value;
    const port = parseInt(document.getElementById('syn-port').value);

    log(`Starting SYN Flood on ${target}:${port}`);
    try {
        await fetch("http://localhost:8000/attack/syn-flood", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ip: target, port, duration: 5 })
        });
        log("SYN Flood started.");
    } catch (err) {
        log("Error: " + err);
    }
}

/* ----------------------------
    TCP Flood
---------------------------- */
async function startTcpFlood() {
    const target = document.getElementById('tcp-target').value;
    const port = parseInt(document.getElementById('tcp-port').value);

    log(`Starting TCP Flood on ${target}:${port}`);
    try {
        await fetch("http://localhost:8000/attack/tcp-flood", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ip: target, port, duration: 5 })
        });
        log("TCP Flood started.");
    } catch (err) {
        log("Error: " + err);
    }
}

/* ----------------------------
    HTTP Stress Test
---------------------------- */
async function startHttpStress() {
    const url = document.getElementById('http-target').value;
    const threads = parseInt(document.getElementById('http-threads').value);

    log(`Starting HTTP Stress Test on ${url} with ${threads} threads`);
    try {
        await fetch("http://localhost:8000/attack/http-stress", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url, threads, duration: 5 })
        });
        log("HTTP Stress Test started.");
    } catch (err) {
        log("Error: " + err);
    }
}

/* ----------------------------
    Port Scan
---------------------------- */
async function startPortScan() {
    const target = document.getElementById('scan-target').value;
    const ports = document.getElementById('scan-ports').value;

    log(`Running Port Scan on ${target} for ports: ${ports}`);
    try {
        const response = await fetch("http://localhost:8000/scan/ports", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ip: target, ports })
        });
        const result = await response.json();
        log(`Scan Result:\n${JSON.stringify(result, null, 2)}`);
    } catch (err) {
        log("Error: " + err);
    }
}

/* ----------------------------
    Extra: Add Log Clear Button
---------------------------- */
const logPanel = document.querySelector('#logs');
const clearBtn = document.createElement('button');
clearBtn.textContent = "Clear Logs";
clearBtn.style.marginTop = "10px";
clearBtn.style.padding = "8px 12px";
clearBtn.style.cursor = "pointer";
clearBtn.onclick = clearLogs;
logPanel.appendChild(clearBtn);
