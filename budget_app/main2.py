# VERSAO 1.0
# app para os tecnicos identificarem mais rapido um orçamento como custo atual da peça
# margem de lucro fixa = 250%
import time

import requests
from bs4 import BeautifulSoup

# receber MARCA, MODELO E DEFEITO do usuario (tecnico)
print("Seja bem vindo ao BudgetCell!")
brand_device = input("Informe a marca do aparelho: \n")
model_device = input("Informe o modelo do aparelho: \n")
fault_device = input("Informe o defeito do aparelho: \n")

# criar um link separado por %20 para inserir no link de pesquisa
info = fault_device+" "+brand_device+" "+model_device
qty_words = info.split()
words_with_term = "%20".join(qty_words)
link_to_search = (
    f"https://flp.distribuidoracp.com.br/index.php?route=product/search&search={words_with_term}")

# acessar o link direto do produto
page = requests.get(link_to_search)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
valores = soup.find(class_='caption')

valores_list = valores.find_all(class_='price')

print(len(valores_list))
