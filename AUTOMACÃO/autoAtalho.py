import pyautogui
import keyboard
import time

# Criar uma função
def tarefa():
    print("Rodando automação")
    time.sleep(2)
    # Abrir meu navegador
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(2)
    # Entrar no Meet
    pyautogui.write("https://meet.google.com/landing?pli=1")
    pyautogui.press("enter")
    time.sleep(3)
    # entrar na sala de reunião
    pyautogui.press("enter")

# Associar essa função a uma combinação de teclas
keyboard.add_hotkey("ctrl+alt+a", tarefa)

keyboard.wait("esc")
