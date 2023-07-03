from googlesearch import search

# Pede ao usuário para digitar a pergunta
query = input("Digite sua pergunta: ")

# Realiza a pesquisa no Google
search_results = search(query, num_results=1)

# Exibe o link da primeira página de resultados que contém a resposta
for url in search_results:
    if "http" in url:
        print("A resposta está neste link: ", url)
        break
