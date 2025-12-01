from docx import Document
from datetime import datetime

documento = Document("f:\DaLucas_Codes\AUTOMACÃO\ARQUIVOS WORD\CONTRATO Emprestado Sem Ele Saber.docx")

nome = "Davi"
cpf = "0123456789"
rua = "Mar de Ross"
nº = "9"
cep = "01234-567"
tipodeserviço = "Rejunte, Pintura e Instalação de Pisos"
valortotal = "5.000"
escrita = "Cinco Mil Reais"
diaultilizados = "15 dias úteis"

referencias = {
    "XXXX": nome,
    "ZZZZ": cpf,
    "MMMM": rua,
    "NNNN": nº,
    "BBBB": cep,
    "KKKK": tipodeserviço,
    "LLLL": valortotal,
    "GGGG": escrita,
    "FFFF": diaultilizados,


}

for paragrafo in documento.paragraphs:
    for codigo in referencias:
        valor = referencias[codigo]
        paragrafo.text = paragrafo.text.replace(codigo, valor)

documento.save(f"Contrato Pego do Pai - SR.{nome}.docx")