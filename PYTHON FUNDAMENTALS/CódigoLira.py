import time
import pyotp
import qrcode

chave_mestre = "T6HJMBUJHD7W3DWU4KE7FRDE6EOFIM3J"

codigo = pyotp.TOTP(chave_mestre)
print(codigo.now())

codigo_usuario = input("Codigo: ")
print(codigo.verify(codigo_usuario))

# link = pyotp.TOTP(chave_mestre).provisioning_uri(name="lira", issuer_name="CodigoPython")
# print(link)
#
# meu_qrcode = qrcode.make(link)
# meu_qrcode.save("qrcode.png")
