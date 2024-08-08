FROM nginx:latest


# Instalar cron, apache2-utils e dos2unix
RUN apt-get update && apt-get install -y cron apache2-utils dos2unix


# Copiar arquivos de configuração do Nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/server.conf /etc/nginx/conf.d/server.conf


# Copiar o script de exclusão
COPY delete_old_files.sh /usr/local/bin/delete_old_files.sh


# Converter o script para formato Unix
RUN dos2unix /usr/local/bin/delete_old_files.sh

# Copiar o arquivo de senha
COPY .htpasswd /etc/nginx/.htpasswd


# Configurar permissões para o script
RUN chmod +x /usr/local/bin/delete_old_files.sh


# Adicionar tarefa cron para excluir arquivos antigos a cada minuto
RUN (crontab -l ; echo "* * * * * /usr/local/bin/delete_old_files.sh") | crontab -


# Iniciar cron e nginx
CMD service cron start && nginx -g 'daemon off;'
