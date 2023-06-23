import time

import pyautogui

# Lista de horarios:
lista_horarios = ["10:52", "11:04", "11:22", "11:57",
                  "12:09", "12:28", "12:39", "12:52", "13:10", "13:22", "13:37", "13:50"]
lista_str = " ". join(lista_horarios)
saudacao = str(time.strftime("%H:%M"))
print("Olá, seja bem vindo ao RoboBlaze1.0!")
print("Agora são: " + saudacao)
print("Os horarios agendados são: " + lista_str)


# Define o valor da sua stake
stake_value = input("Digite sua stake: ")

while True:
    # Verifica o horário atual
    hora_atual = time.strftime("%H:%M")
    if hora_atual in lista_horarios:

        # Ir para desktop
        pyautogui.keyDown('win')
        pyautogui.press('m')
        pyautogui.keyUp('win')
        time.sleep(1)

        # Abre o chrome (x=1304, y=247)
        pyautogui.doubleClick(1304, 247)

        # Espera o carregamento da página
        time.sleep(2)

        # Maximiza a página (x=1293, y=25)
        pyautogui.click(1293, 25)
        time.sleep(1)

        # Acessa a blaze (x=193, y=50)
        pyautogui.click(193, 50)
        pyautogui.typewrite("https://blaze.com/pt/games/double")
        pyautogui.press('enter')
        time.sleep(3)

        # VERIFICAR SE JÁ TEVE BRANCO NOS ULTIMOS 4 GIROS (usar cor como filtro?)

        # Clica em 'auto'
        pyautogui.click(489, 267)
        time.sleep(1)

        # Clica em 'x14'
        pyautogui.click(425, 418)
        time.sleep(1)

        # Digita stake_value em 'Quantia'
        pyautogui.click(336, 336)
        pyautogui.typewrite(stake_value, interval=0.1)
        time.sleep(1)

        # Digita 13 em 'Total Apostas'
        pyautogui.click(347, 503)
        pyautogui.typewrite("13", interval=0.1)
        time.sleep(3)

        # Clica em Iniciar Auto-Aposta
        pyautogui.click(422, 568)
        time.sleep(420)  # tempo de girar 12x + 1min de sobra

        # CLICAR EM 'CANCELAR' QUANDO CAIR BRANCO (usar cor como filtro?)

        # Fecha o chrome
        pyautogui.click(1338, 13)

    else:
        # Espera 1 minuto antes de verificar novamente o horário
        time.sleep(60)
