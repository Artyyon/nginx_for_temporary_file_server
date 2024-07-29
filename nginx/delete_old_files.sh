#!/bin/sh

# Diretório onde os arquivos são armazenados
UPLOAD_DIR="/usr/share/nginx/html/files"

# Encontrar e excluir arquivos com mais de 10 minutos
find "$UPLOAD_DIR" -type f -mmin +10 -exec rm -f {} \;
