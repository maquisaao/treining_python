import requests
from bs4 import BeautifulSoup

# URL do site
url = 'https://flp.distribuidoracp.com.br/'

# Parâmetros da pesquisa
params = {
    'q': 'tela iphone 11'
}

# Fazendo a requisição GET com os parâmetros
response = requests.get(url, params=params)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Criando o objeto BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrando o primeiro valor na página
    primeiro_valor = soup.find("span", class_="price").text.strip()

    # Exibindo o valor para o usuário
    print('O primeiro valor encontrado é:', primeiro_valor)
else:
    print('Erro ao fazer a requisição:', response.status_code)
