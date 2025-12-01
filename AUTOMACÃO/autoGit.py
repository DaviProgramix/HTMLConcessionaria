### Entra no GitHub

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) #headless
    pagina = navegador.new_page()
    pagina.goto("https://github.com/?locale=pt-BR")
    pagina.locator('xpath=/html/body/div[1]/div[3]/header/div/div[2]/div/div/div/a').click()
    pagina.fill('xpath=//*[@id="login_field"]',"davilucasbaiermachado06@gmail.com")
    pagina.fill('xpath=//*[@id="password"]',"Deumanove19")
    pagina.locator('xpath=//input[@name="commit"]').click()
    time.sleep(10)
    