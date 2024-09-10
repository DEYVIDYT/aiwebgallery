import socket
import threading

peers = set()
peer_port = 5000
discovery_port = 5001

def discover():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', discovery_port))
    while True:
        data, addr = s.recvfrom(1024)
        if data.decode() == 'DISCOVER':
            s.sendto(b'RESPOND', addr)
            peers.add(addr)
            print(f"Peer discovered: {addr}")

def announce():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while True:
        s.sendto(b'DISCOVER', ('<broadcast>', discovery_port))
        print("Announced discovery")
        time.sleep(10)

if __name__ == "__main__":
    threading.Thread(target=discover).start()
    threading.Thread(target=announce).start()
