### Bot no Computador - pyautogui
import pyautogui
import time

pyautogui.PAUSE = 2

# Abrir a Ferramenta/Sistema/Programa
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")

# Preencher o login
time.sleep(3)
pyautogui.click(x=654, y=326)
pyautogui.write("Davi")

# Preencher a senha
pyautogui.click(x=725, y=375)
pyautogui.write("senha")

# Clicar em fazer login
pyautogui.click(x=632, y=486)

import time

time.sleep(3)
pyautogui.position()
