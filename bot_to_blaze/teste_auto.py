import time

import pyautogui

# Lista de horarios:
lista_horarios = ["03:30", "03:48", "04:05",
                  "04:22", "04:51"]
lista_str = " ". join(lista_horarios)
saudacao = str(time.strftime("%H:%M"))
print("Olá, seja bem vindo ao RoboBlaze1.0!")
print("Agora são: " + saudacao)
print("Os horarios agendados são: " + lista_str)


print("")

# Define o valor da sua stake
# stake_value = input("Digite sua stake: ")

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

        # Clica em 'auto' (x=489, y=267)
        pyautogui.click(489, 267)
        time.sleep(1)

        # Clica em 'x14' (x=425, y=418)
        pyautogui.click(425, 418)
        time.sleep(1)

        # Digita stake_value em 'Quantia' (x=336, y=336)
        # pyautogui.click(336, 336)
        # pyautogui.typewrite(stake_value, interval=0.1)
        # time.sleep(1)

        # Digita 13 em 'Total Apostas' (x=347, y=503)
        pyautogui.click(347, 503)
        pyautogui.typewrite("13", interval=0.1)
        time.sleep(1)

        # Clica em Iniciar Auto-Aposta (x=422, y=568)
        pyautogui.click(422, 568)
        time.sleep(50)

        # Fecha o chrome (x=1338, y=13)
        pyautogui.click(1338, 13)

    else:
        # Espera 1 minuto antes de verificar novamente o horário
        time.sleep(60)
