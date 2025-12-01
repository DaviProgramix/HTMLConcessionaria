import pandas as pd

df = pd.read_excel("f:/DaLucas_Codes/AUTOMACÃO/ARQUIVOS EXCEL/LojaDoReMi.xlsx")
df["total"] = df["Quantidades"] * df["Preço"]
tvp = df.groupby("Produtos")[["Quantidades", "Preço", "total"]].sum().reset_index()

print(tvp)
