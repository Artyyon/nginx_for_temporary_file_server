### Utilização do Servidor de Arquivos Temporários com Nginx


#### Introdução

Este documento fornece instruções detalhadas sobre como utilizar o servidor de arquivos temporários configurado com Nginx. Ele inclui exemplos de código para envio e recuperação de arquivos, bem como instruções para garantir a autenticação e o acesso seguro.


#### Pré-requisitos

- Um servidor de arquivos temporários configurado com Nginx conforme a documentação anterior.
- Python instalado no seu sistema.
- Biblioteca `requests` instalada (pode ser instalada usando `pip install requests`).


#### Enviando Arquivos para o Servidor

Para enviar arquivos para o servidor, você pode utilizar o seguinte código Python. Este exemplo cria um arquivo com um nome aleatório e envia seu conteúdo para o servidor usando uma requisição `PUT`.

```python
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
```


##### Explicação

- **file_name**: Gera um nome aleatório para o arquivo a ser enviado.
- **file_data**: Gera um conteúdo aleatório para o arquivo.
- **upload_url**: Define a URL do endpoint de upload.
- **username** e **password**: Credenciais de autenticação para o upload.
- **requests.put**: Envia o arquivo para o servidor com autenticação básica.


#### Recuperando Arquivos do Servidor

Para recuperar um arquivo enviado ao servidor, você pode utilizar o seguinte código Python. Este exemplo recupera o conteúdo do arquivo previamente enviado.

```python
# Recupera o arquivo pela requisição GET
file_url = f'http://localhost:8080/get/{file_name}'

file_response = requests.get(file_url)

print('RECUPERAÇÃO DE ARQUIVO')
print(f'File Status Code: {file_response.status_code}')
print(f'File Content: {file_response.text}')
```


##### Explicação

- **file_url**: Define a URL do endpoint de recuperação do arquivo.
- **requests.get**: Recupera o arquivo do servidor.


#### Utilização com cURL

Você também pode utilizar cURL para enviar e recuperar arquivos. Abaixo estão os comandos para realizar essas operações.


##### Enviando Arquivos com cURL

```sh
curl -u xDz6tQGa55yGu7q:qFUtf9jnyV5Y4b6 -X PUT --upload-file user.txt http://localhost:8080/upload/user.txt -v
```


##### Explicação

- **-u**: Especifica as credenciais de autenticação.
- **-X PUT**: Define o método HTTP como PUT.
- **--upload-file**: Especifica o arquivo a ser enviado.
- **-v**: Habilita o modo verbose para exibir detalhes da requisição.


##### Recuperando Arquivos com cURL

```sh
curl http://localhost:8080/get/user.txt -v
```


##### Explicação

- Este comando envia uma requisição GET para recuperar o arquivo `user.txt` do servidor.


#### Considerações Finais

Este guia fornece exemplos práticos de como utilizar o servidor de arquivos temporários configurado com Nginx. Seguindo estas instruções, você poderá enviar e recuperar arquivos de maneira eficiente e segura.


<sub>Ultima atualização 29/07/2024.</sub>
