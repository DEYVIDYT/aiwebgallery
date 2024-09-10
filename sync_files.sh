#!/bin/bash

source_path="/storage/emulated/0/IPTVP2P/"
peer_port=5000

# Função para sincronizar arquivos
sync_files() {
    rsync -avz $source_path user@peer_ip:/path/to/destination/
}

# Função para iniciar o servidor
start_server() {
    nc -l -p $peer_port > /tmp/incoming_file
}

# Função para escutar conexões
listen_for_files() {
    while true; do
        nc -l -p $peer_port | while read file; do
            if [ -f $source_path$file ]; then
                rsync -avz $source_path$file user@peer_ip:/path/to/destination/
            fi
        done
    done
}

sync_files
start_server
listen_for_files
