from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess
import time
import requests
import socket

class Watcher(FileSystemEventHandler):
    def __init__(self, file_path, discovery_url):
        self.file_path = file_path
        self.discovery_url = discovery_url
    
    def on_modified(self, event):
        if event.src_path == self.file_path:
            print(f"Detected changes in {self.file_path}")
            self.sync_file()

    def sync_file(self):
        print(f"Syncing file {self.file_path} with peers")
        peers = self.get_peers()
        for peer in peers:
            # Exemplo de uso do rsync:
            subprocess.run(["rsync", "-av", self.file_path, f"user@{peer}:/path/to/destination"])

    def get_peers(self):
        try:
            response = requests.get(f"{self.discovery_url}/peers")
            response.raise_for_status()
            data = response.json()
            return data.get("peers", [])
        except requests.RequestException as e:
            print(f"Error fetching peers: {e}")
            return []

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

if __name__ == "__main__":
    path = "/storage/emulated/0/IPTVP2P/txt.php"
    discovery_url = "http://your-discovery-server-ip:5000"  # Atualize com o IP do seu servidor de descoberta
    
    local_ip = get_local_ip()
    try:
        response = requests.post(f"{discovery_url}/register", json={"ip": local_ip})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error registering with discovery server: {e}")

    event_handler = Watcher(path, discovery_url)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(path), recursive=False)
    observer.start()
    print(f"Watching for changes in {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
