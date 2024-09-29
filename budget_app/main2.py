#versão 2

import re

import httpx
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

# fazer login pra acessar os valores


def Sugador():
    with httpx.Client(base_url="https://flp.distribuidoracp.com.br") as client:
        client.post(
            "/conta/acessar",
            data={"email": "login",
                  "password": "senha"},
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

            print(f"Nome: {nome[0:30]}")
            print(f"Preço: {preco[0:30]}")
            print()


Sugador()

# verificar quais das 3 opçoes é a correta
# calcular o valor final baseado na escolha
# perguntar se quer fazer outro orçamento
