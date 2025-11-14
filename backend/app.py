from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Attack modules
from attacks.syn_flood import syn_flood
from attacks.tcp_connect_flood import tcp_connect_flood
from attacks.http_stress import http_stress
from attacks.port_scan import port_scan

app = FastAPI(title="NetProbe Backend", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "NetProbe backend running"}


# ---------------------- #
#      REQUEST MODELS    #
# ---------------------- #

class SynFloodRequest(BaseModel):
    ip: str
    port: int
    duration: int = 5


class TCPFloodRequest(BaseModel):
    ip: str
    port: int
    duration: int = 5


class HTTPStressRequest(BaseModel):
    url: str
    threads: int = 50
    duration: int = 5


class PortScanRequest(BaseModel):
    ip: str
    start_port: int = 1
    end_port: int = 1024


# ---------------------- #
#      ENDPOINTS         #
# ---------------------- #

@app.post("/attack/syn-flood")
def run_syn_flood(data: SynFloodRequest):
    """Run SYN Flood Attack"""
    return syn_flood(data.ip, data.port, data.duration)


@app.post("/attack/tcp-flood")
def run_tcp_flood(data: TCPFloodRequest):
    """Run TCP Connect Flood Attack"""
    return tcp_connect_flood(data.ip, data.port, data.duration)


@app.post("/attack/http-stress")
def run_http_stress(data: HTTPStressRequest):
    """Run HTTP GET Stress Test"""
    return http_stress(data.url, data.threads, data.duration)


@app.post("/scan/ports")
def run_port_scan(data: PortScanRequest):
    """Run TCP Port Scan"""
    return port_scan(data.ip, data.start_port, data.end_port)
