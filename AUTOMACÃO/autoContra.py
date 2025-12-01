from docx import Document
from datetime import datetime

documento = Document("f:\DaLucas_Codes\AUTOMACÃO\ARQUIVOS WORD\Contrato.docx")

nome = "Davi"
item1 = "Carro"
item2 = "Notebook"
item3 = "Celular"

referencias = {
    "XXXX": nome,
    "YYYY": item1,
    "ZZZZ": item2,
    "WWWW": item3,
    "DD": str(datetime.now().day),
    "MM": str(datetime.now().month),
    "AAAA": str(datetime.now().year),
}

for paragrafo in documento.paragraphs:
    for codigo in referencias:
        valor = referencias[codigo]
        paragrafo.text = paragrafo.text.replace(codigo, valor)

documento.save(f"Contrato - {nome}.docx")