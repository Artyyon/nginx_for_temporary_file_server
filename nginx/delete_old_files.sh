#!/bin/sh

# Diretório onde os arquivos são armazenados
UPLOAD_DIR="/usr/share/nginx/html/files"

# Log de execução
echo "$(date) - Executando script de exclusão" >> /var/log/nginx/delete_files.log

# Verificar o diretório e os arquivos
ls -l "$UPLOAD_DIR" >> /var/log/nginx/delete_files.log

# Encontrar e excluir arquivos com mais de 10 minutos
find "$UPLOAD_DIR" -type f -mmin +10 -exec rm -f {} \; 2>> /var/log/nginx/delete_files.log
