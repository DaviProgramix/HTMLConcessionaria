import openpyxl

def atualizar_planilha():
    workbook = openpyxl.load_workbook("f:\DaLucas_Codes\AUTOMACÃO\ARQUIVOS EXCEL\dados.xlsx")
    aba = workbook.active
    aba.append(["Davi", 31, "Programação"])
    workbook.save("dados.xlsx")
    print("Planilha Atualizada")

atualizar_planilha()

