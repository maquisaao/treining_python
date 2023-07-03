import re
import csv
import numpy as np
import pandas as pd
import requests
import httpx
from bs4 import BeautifulSoup
import time

print("Seja bem vindo ao BudgetCell!")
# fazer login
login=input("Login:")
senha=input("Senha:")
loop= "s"
while loop == "s":

    # receber MARCA, MODELO E DEFEITO do usuario (tecnico)
    model_device = input("Informe o modelo do aparelho: \n")
    fault_device = input("Informe o defeito do aparelho: \n")

    # criar um link separado por %20 para inserir no link de pesquisa
    info = fault_device+" "+model_device
    qty_words = info.split()
    words_with_term = "%20".join(qty_words)
    link_to_search = (
        f"https://flp.distribuidoracp.com.br/index.php?route=product/search&search={words_with_term}")

    # fazer login pra acessar os valores
    with httpx.Client(base_url="https://flp.distribuidoracp.com.br") as client:
        client.post(
            "/conta/acessar",
            data={"email": login,
                    "password": senha},
            headers={
                "origin": "https://flp.distribuidoracp.com.br",
                "referer": "https://flp.distribuidoracp.com.br/conta/acessar",
            },
        )

        # buscar as entradas do usuário
        busca = client.get(
            "/index.php", params={"route": "product/search", "search": info}
        )

        # usar a classe price e retornar os valores iniciados com R$
        resultado = BeautifulSoup(busca.text, "html.parser")
        produtos = resultado.find_all("div", "product-list")
        for produto in produtos[:3]:  # Retorna os três primeiros produtos
            # h4 é a div que está o texto do item
            nome = produto.find("h4").text.strip()
            # price é a classe de onde ta o preço
            preco = produto.find("p", "price").text.strip()
            # trazer somento o texto que tem valor (R$)
            preco_valor = re.search(r"R\$[\d\.,]+", preco)
            if preco_valor:
                preco = preco_valor.group()

            print(f"Nome: {nome[0:100]}")
            print(f"Preço: {preco[0:30]}")

    # verificar quais das 3 opçoes é a correta
    valor_escolhido=float(input("Qual o valor do item? "))

    valor_final_cartao=valor_escolhido*2.4
    valor_final_pix=valor_escolhido*2.2
    print(f"O valor a ser cobrado é de R$ {valor_final_cartao:.2f} se for no cartao.")
    print(f"O valor a ser cobrado é de R$ {valor_final_pix:.2f} se for no pix ou dinheiro.")

    loop=input("Gostaria de fazer outro orçamento?\n")

time.sleep(10)