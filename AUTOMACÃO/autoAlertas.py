# Cotação do dolar for menor que 5.20
# NÃO DEU CERTO !!!!!!!

import requests

# Pegar a informação que você quer
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)

# Enviar um aviso - email
import smtplib
import email.message

def enviar_email(cotacao):  
    corpo_email = f"""
    <p>Dólar está abaixo de R$5.20. Cotação atual : R$ {cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Dólar está hoje de R$5.20"
    msg['From'] = 'davilucasbaiermachado06@gmail.com'
    msg['To'] = 'davilucasbaiermachado06@gmail.com'
    password = 'senha' # NAO CONSIGO USAR
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao < 5.20:
    enviar_email(cotacao)
