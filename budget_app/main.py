import time

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("screen.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI


MeuAplicativo().run()


# receber marca, modelo e defeito
marca = input("Qual a marca? \n")
modelo = input("Qual o modelo? \n")
defeito = input(
    "Qual o defeito?\n[T] Tela\n[B] Bateria\n[C] Conector de Carga\n ")
fator_confirmacao = "N"

# encaminhar pro site com o link ja pronto pra pesquisa (condicional)
# link: https://flp.distribuidoracp.com.br/index.php?route=product/search&search=tela%20apple%20iphone%206s

if defeito == "T":
    print("Você precisa de orçamento para troca de Tela do "+marca+" "+modelo)
    print("Clique no link abaixo e retorne com o valor.\n")
    print("https://flp.distribuidoracp.com.br/index.php?route=product/search&search=display" +
          "%20"+marca+"%20"+modelo)

if defeito == "B":
    print("Você precisa de orçamento para troca de Bateria do "+marca+" "+modelo)
    print("Clique no link abaixo e retorne com o valor.\n")
    print("https://flp.distribuidoracp.com.br/index.php?route=product/search&search=bateria" +
          "%20"+marca+"%20"+modelo)

if defeito == "C":
    print("Você precisa de orçamento para troca de Conector de carca do "+marca+" "+modelo)
    print("Clique no link abaixo e retorne com o valor.\n")
    print("https://flp.distribuidoracp.com.br/index.php?route=product/search&search=conector" +
          "%20"+marca+"%20"+modelo)

busca_valor = float(input("Qual o custo?\n"))
valor_original = float(busca_valor*3.5)
valor_desconto = float(busca_valor*3)
valor_pix = float(busca_valor*2.6)

print(f"Valor sugerido é de\n R${valor_original:,.2f} no cartao até 3x\nR${valor_desconto:,.2f} no debito ou credito a vista\nR${valor_pix:,.2f} no pix ou dinheiro")

time.sleep(10)
