from datetime import datetime
import pytz

texto_data = "18/11/2025 10:00"
minha_data = datetime.strptime(texto_data, "%d/%m/%Y %H:%M")
print(minha_data)

fuso_horario = pytz.timezone("America/Sao_Paulo")
minha_data_com_fuso = fuso_horario.localize(minha_data)
print(minha_data_com_fuso)

novo_fuso = pytz.timezone("Europe/Paris")
minha_data_novo_fuso = minha_data_com_fuso.astimezone(novo_fuso)
print(minha_data_novo_fuso)

print(minha_data_novo_fuso.dst())

nf = pytz.timezone("Europe/London")
n = minha_data_com_fuso.astimezone(nf)
print(n)

print(n.dst())


nf2 = pytz.timezone("Asia/Tokyo")
n2 = minha_data_com_fuso.astimezone(nf2)
print(n2)

print(n2.dst())