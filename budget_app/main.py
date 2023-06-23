# receber marca, modelo e defeito
marca = input("Qual a marca? \n")
modelo = input("Qual o modelo? \n")
defeito = input(
    "Qual o defeito?\n[T] Tela\n[B] Bateria\n[C] Conector de Carga\n ")
fator_confirmacao = "N"

# confirmar a entrada com usuario (condicional)
while fator_confirmacao == confirmacao:
    if defeito == "T":
        print("Você precisa de orçamento para troca de Tela do "+marca+" "+modelo)
        confirmacao = input("Está correto?\n[S] Sim\n[N] Não\n")

    if defeito == "B":
        print("Você precisa de orçamento para troca de Bateria do "+marca+" "+modelo)
        confirmacao = input("Está correto?\n[S] Sim\n[N] Não\n")

    if defeito == "C":
        print(
            "Você precisa de orçamento para troca de Conector de carca do "+marca+" "+modelo)
        confirmacao = input("Está correto?\n[S] Sim\n[N] Não\n")

print("usar o nao passou pra ca.")


# encaminhar pro site com o link ja pronto pra pesquisa
# receber valor da peça
# calcular valor final e mostrar ao usuario
