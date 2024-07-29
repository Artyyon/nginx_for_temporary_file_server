import requests
import random

# Cria um nome para o arquivo
file_name = ''.join(random.choices('0123456789ABCDEF', k=8))
file_name += '.txt'

# Dados a serem enviados no corpo da requisição
file_data = ''.join(random.choices('0123456789ABCDEF', k=8))

# URL do endpoint de upload
upload_url = f'http://localhost:8080/upload/{file_name}'

# Credenciais de autenticação
username = 'xDz6tQGa55yGu7q'
password = 'qFUtf9jnyV5Y4b6'

# Enviar requisição PUT com o conteúdo do arquivo e autenticação básica
response = requests.put(upload_url, data=file_data, auth=(username, password))

print("CRIAÇÃO DE ARQUIVO")
print(f'Upload Status Code: {response.status_code}')
print(f'Upload Response: {response.text}')

# Recupera o arquivo pela requisição GET
file_url = f'http://localhost:8080/get/{file_name}'

file_response = requests.get(file_url)

print('RECUPERAÇÃO DE ARQUIVO')
print(f'File Status Code: {file_response.status_code}')
print(f'File Content: {file_response.text}')
