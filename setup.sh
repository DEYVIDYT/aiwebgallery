#!/bin/bash

# Atualiza o Termux e instala Python
pkg update
pkg upgrade
pkg install python

# Instala as dependências do projeto
pip install -r requirements.txt

echo "Configuração completa. Pronto para usar!"
