import pandas as pd

produtos = []

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    
    continuar = input("Deseja adicionar outro produto? (s/n): ").lower()
    if continuar != "s":
        break

df = pd.DataFrame(produtos)
df.to_excel("Compras1.xlsx", index=False)