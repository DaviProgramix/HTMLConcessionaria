import openpyxl

def atualizar_planilha():
    workbook = openpyxl.load_workbook(r"f:\DaLucas_Codes\AUTOMACÃO\ARQUIVOS EXCEL\DadosCarro.xlsx")
    aba = workbook.active

    aba.append(["Fiat","Argo", "Hatch", 85.000, 2024, "Metálica", "1.3 Flex"])
    aba.append(["Chevrolet","Onix", "Hatch", 110.000, 2025, "Metálica", "1.0 Turbo Flex"])
    aba.append(["Volkswagen","T-Cross Comfortline", "SUV", 160.000, 2025, "Metálica", "1.0 TSI Flex"])
    aba.append(["Toyota","Corolla Altis híbrido", "Sedan", 190.000, 2021, "Vermelho", "1.8 híbrido"])
    aba.append(["Honda","Civic Touring", "Sedan", 230.000, 2025, "Preto", "1.5 Turbo"])
    workbook.save("DadosCarro2.xlsx")
    print("Planilha feita com sucesso")

atualizar_planilha()