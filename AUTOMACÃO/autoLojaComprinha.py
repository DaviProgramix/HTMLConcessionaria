import pandas as pd

df = pd.read_excel("f:/DaLucas_Codes/AUTOMACÃO/ARQUIVOS EXCEL/Loja Comprinha.xlsx")
df["total"] = df["Quantidades"] * df["Preço Unitário"]
tvp = df.groupby("Produtos")[["Quantidades", "Preço Unitário", "total"]].sum().reset_index()
print(tvp)
