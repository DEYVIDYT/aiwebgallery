import time
import os
import hashlib

file_path = '/storage/emulated/0/IPTVP2P/txt.php'
peers = set()  # Adicione peers descobertos

def get_file_hash(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def monitor_file():
    last_hash = get_file_hash(file_path)
    while True:
        time.sleep(10)
        new_hash = get_file_hash(file_path)
        if new_hash != last_hash:
            last_hash = new_hash
            for peer in peers:
                # Enviar alterações para os peers
                pass
            print("File changed, syncing with peers")

if __name__ == "__main__":
    monitor_file()
