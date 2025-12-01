import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Parabéns</p>
    <p>Parabéns meu jovem</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Olá"
    msg['From'] = 'davilucasbaiermachado06@gmail.com'
    msg['To'] = 'davilucasbaiermachado06@gmail.com'
    password = 'abcd efgh ijkl mnop' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')