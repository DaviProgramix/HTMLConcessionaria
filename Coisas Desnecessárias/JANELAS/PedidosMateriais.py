import datetime as dt
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Carrega planilha já existente
materiais = pd.read_excel(
    'f:/DaLucas_Codes/PYTHON FUNDAMENTALS/Materiais.xlsx',
    engine='openpyxl'
)

lista_tipos = ["Galão", "Caixa", "Saco", "Unidade"]
lista_codigos = []

janela = tk.Tk()

# Função de criação de código
def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()

    data_criacao = dt.datetime.now().strftime("%d/%m/%Y %H:%M")

    codigo = materiais.shape[0] + len(lista_codigos) + 1
    codigo_str = f"COD-{codigo}"

    # Armazena temporariamente até a janela ser fechada
    lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao))

    # Limpa os campos na tela
    entry_descricao.delete(0, tk.END)
    entry_quant.delete(0, tk.END)
    combobox_selecionar_tipo.set("")

# Configuração da Janela
janela.title("Pedidos de Materiais")

label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='NSWE', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='NSWE', columnspan=4)

label_tipo_unidade = tk.Label(text="Tipo da Unidade do Material")
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='NSWE', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='NSWE', columnspan=2)

label_quant = tk.Label(text="Quantidade na Unidade do Material")
label_quant.grid(row=4, column=0, padx=10, pady=10, sticky='NSWE', columnspan=2)

entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, padx=10, pady=10, sticky='NSWE', columnspan=2)

botao_criar_codigo = tk.Button(text="Pedir ", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='NSWE', columnspan=4)

# Abre a janela
janela.mainloop()

# Quando a janela fecha gera DataFrame final e salva
novo_material = pd.DataFrame(
    lista_codigos,
    columns=['Código', 'Descrição', 'Tipo', 'Quantidade', 'Data Pedido']
)

# Junta com os dados existentes
materiais = pd.concat([materiais, novo_material], ignore_index=True)

# Salva arquivo final
materiais.to_excel(
    'f:/DaLucas_Codes/PYTHON FUNDAMENTALS/Materiais.xlsx',
    index=False
) 

print("Pedidos Feitos com Sucesso!")
