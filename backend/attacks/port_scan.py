import socket
import threading

open_ports = []

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    except:
        pass

def port_scan(ip: str, start_port: int = 1, end_port: int = 1024, threads_count: int = 200):
    global open_ports
    open_ports = []

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        t.start()
        threads.append(t)

        if len(threads) >= threads_count:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    return {
        "status": "Port scan completed",
        "target": ip,
        "total_ports_checked": end_port - start_port,
        "open_ports": open_ports,
    }
