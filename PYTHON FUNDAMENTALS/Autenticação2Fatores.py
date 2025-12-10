import time
import pyotp
import qrcode

chave_mestre = "VZUGR6XUCWPLAW2VMOMYK5YI45MVVEVM"

codigo = pyotp.TOTP(chave_mestre)
# print(codigo.now())

codigo_usuario = input("Código: ")
print(codigo.verify(codigo_usuario))

link = pyotp.TOTP(chave_mestre).provisioning_uri(name="Davi", issuer_name="CódigoPython")

meu_qrcode = qrcode.make(link)
meu_qrcode.save("qrcode.png")
