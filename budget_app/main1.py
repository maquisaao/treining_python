# VERSAO 1.0
# app para os tecnicos identificarem mais rapido um orçamento como custo atual da peça
# margem de lucro fixa = 250%
import time

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

# encaminhar pro link e pedir o valor do produto
print("Acesse o link e volte com o valor do item.")
print(link_to_search)
value_found = float(input("Qual o valor? \n"))

# brincar com tempo de processamento
print("Calculando valores")
time.sleep(2)
print("...")
time.sleep(2)
print("...")
time.sleep(2)
print("...")
time.sleep(2)
print("Pronto. Aqui estão os valores:\n")

# retornar valor final em 3 formas de pagamento (cartao 3x / debito credito a vista / pix dinheiro)
# sem choro ate 3x = .3,5 / com choro = .3 / com muito choro no pix = .2,5
without_cry = float(value_found*3.5)
with_cry = float(value_found*3)
with_a_lot_of_crying = float(value_found*2.5)
print(
    f"Se nao tiver choro nenhum dá pra fazer por >>R$ {without_cry}<<\nSe tiver um chorinho da pra fazer por R$ >>{with_cry}<<\nJá se for na base de muito choro e for no pix da pra fazer por R$ >>{with_a_lot_of_crying}<<\n")
