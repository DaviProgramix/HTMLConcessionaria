### Entra no Khan Academy


import pyautogui
import time

pyautogui.PAUSE = 5.0
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(5)

pyautogui.write("khanacademy.org")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=992, y=238)
time.sleep(3)
pyautogui.click(x=992, y=253)
time.sleep(3)
pyautogui.click(x=577, y=300)
time.sleep(3)
pyautogui.click(x=704, y=550)
time.sleep(3)
pyautogui.click(x=604, y=404)
time.sleep(3)
pyautogui.click(x=587, y=682)
