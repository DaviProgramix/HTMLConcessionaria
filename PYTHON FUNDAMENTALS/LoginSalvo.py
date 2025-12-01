import pandas as pd
import os

i = input("Digite Um Instrumento Musical: ")
q = int(input("Digite A Quantidade: "))
p = float(input("Digite O Preço Que O Senhor Queira Pagar: "))

novo = pd.DataFrame({
    "Instrumento Musical": [i],
    "Quantidade": [q],
    "Preço": [p]
})

arquivo = "Instrumentos Musicais.xlsx"

if p < 150:
    print("Seu pedido foi recusado")
    print("Nada foi registrado.")
else:
    print("Pedido aceito!")

    if os.path.exists(arquivo):
        antigo = pd.read_excel(arquivo)
        df = pd.concat([antigo, novo], ignore_index=True)
    else:
        df = novo

    df.to_excel(arquivo, index=False)
    print("Instrumento registrado com sucesso!")
