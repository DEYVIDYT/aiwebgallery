#!/bin/bash

# Atualize o Termux e instale pacotes necessários
pkg update
pkg upgrade
pkg install -y python git rsync curl cronie

# Clonar o repositório GitHub


# Configurar permissões e iniciar scripts
chmod +x ~/p2p-scripts/sync_files.sh
chmod +x ~/p2p-scripts/discover_peers.py
chmod +x ~/p2p-scripts/monitor_changes.py

# Iniciar os scripts na inicialização
echo 'python ~/p2p-scripts/discover_peers.py &' >> ~/.bashrc
echo 'python ~/p2p-scripts/monitor_changes.py &' >> ~/.bashrc
echo 'sh ~/p2p-scripts/sync_files.sh &' >> ~/.bashrc

# Iniciar cron para execução periódica
crond
