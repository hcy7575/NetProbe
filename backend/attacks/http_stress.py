import requests
import threading
import time

def http_stress(target_url: str, threads_count: int = 100, duration: int = 5):

    def attack():
        end = time.time() + duration
        while time.time() < end:
            try:
                requests.get(target_url, timeout=0.1)
            except:
                pass

    threads = []
    for _ in range(threads_count):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return {
        "status": "HTTP Stress Test completed",
        "target": target_url,
        "threads_used": threads_count,
        "duration_seconds": duration,
    }
