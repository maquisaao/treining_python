import time

import pyautogui

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

# Printa a pagina
img = pyautogui.screenshot()
