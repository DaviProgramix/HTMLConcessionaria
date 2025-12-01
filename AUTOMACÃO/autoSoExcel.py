import openpyxl

def atualizar_planilha():
    workbook = openpyxl.load_workbook(r"f:\DaLucas_Codes\AUTOMACÃO\ARQUIVOS EXCEL\DaviL2.xlsx")
    aba = workbook.active

    aba.append(["Davi", 30, "Programador", "M", "Java Script, Python"])
    aba.append(["Pedro", 33, "programador", "M", "Java Script, Python, Java"])
    aba.append(["Mailson", 53, "Pedreiro", "M", "Votoran, Amanco, Tigre, Coral"])
    aba.append(["Samara", 56, "Rainha", "F", "Reinar"])
    workbook.save("DaviL2.xlsx")
    print("Planilha feita com sucesso")

atualizar_planilha()