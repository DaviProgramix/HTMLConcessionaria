from imap_tools import MailBox, AND

usuario = "davilucasbaiermachado06@gmail.com"
senha = ""  # senha de app, NÃO compartilhe com ninguém!

with MailBox("imap.gmail.com").login(usuario, senha) as mailbox:
    # Pegar emails
    emails = mailbox.fetch(AND(from_="davilucasbaiermachado06@gmail.com", to="daviduo203@gmail.com"))
    for email in emails:
        print(email.subject)
        print(email.text)

    # Pegar anexos
    emails_com_anexo = mailbox.fetch(AND(from_="davilucasbaiermachado06@gmail.com"))
    for email in emails_com_anexo:
        for anexo in email.attachments:
            if "RelatorioExcel" in anexo.filename:
                with open("RelatorioExcel.xlsx", "wb") as arquivo_excel:
                    arquivo_excel.write(anexo.payload)
                print("Anexo salvo:", anexo.filename)

