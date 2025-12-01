import win32com.client as win32

# Criar a intregação com o outlook

outlook = win32.Dispatch('outlook.application') 
# Criar um email
email = outlook.CreateItem(0)

# Configurar as informações do seu email
email.to = "davilucasbaiermachado06@gmail.com"
email.Subject = "Email automático do python"
email.HTMLBody = """
<p>Olá Davi, aqui é o email automático em python que você fez</p>

<p>Parabéns meu caro jovem, pelo seu esforço e pela sua mente brilhante e inteligente, você conseguiu programar um email automático que manda qualquer coisa e para qualquer pessoa.</p>
<p>Eu vim aqui para lhe dar um parabéns pelo seu esforçoe dedicação.</p>

<p>Obrigado pela atenção,</p>
<p>Email Automático em python</p>
""" ### AS Aspas triplas (""") você pode fazer quantas linhas vc quer e o <p>TEM QUE POR NO INÍCIO DE CADA LINHA e o </p>TEM QUE POR NO FINAL DE CADA LINHA !!!!!!!!!!

email.Send()
print("Email Enviado")