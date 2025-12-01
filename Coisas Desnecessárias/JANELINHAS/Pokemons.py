import datetime as dt
import tkinter as tk
from tkinter import ttk
import pandas as pd

pokemons = pd.read_excel(
    'f:/DaLucas_Codes/JANELINHAS/Pokemons.xlsx',
    engine='openpyxl'
)

lista_tipos = [
    "Normal", "Fogo", "Água", "Planta", "Elétrico", "Gelo", "Lutador", "Voador",
    "Venenoso", "Terra", "Pedra", "Psíquico", "Inseto", "Fantasma", "Aço",
    "Dragão", "Sombrio", "Fada"
]

lista_codigos = []

janela = tk.Tk()
janela.title("Pokémons")


def inserir_codigo():
    nivel = entry_nv.get()
    tipo = combobox_selecionar_tipo.get()
    nome = entry_nome.get()
    apelido = entry_apelido.get()
    data = dt.datetime.now().strftime("%d/%m/%Y %H:%M")

    codigo = pokemons.shape[0] + len(lista_codigos) + 1
    codigo_str = f"Pokemon-{codigo}"

    lista_codigos.append((nome, tipo, nivel, data))

    entry_nv.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_apelido.delete(0, tk.END)
    combobox_selecionar_tipo.set("")


label_nome = tk.Label(text="Qual o Pokémon")
label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='NSWE', columnspan=4)

entry_nome = tk.Entry()
entry_nome.grid(row=2, column=0, padx=10, pady=10, sticky='NSWE', columnspan=4)

label_apelido = tk.Label(text="Qual o Nome")
label_apelido.grid(row=3, column=0, padx=10, pady=10, sticky='NSWE', columnspan=4)

entry_apelido = tk.Entry()
entry_apelido.grid(row=4, column=0, padx=10, pady=10, sticky='NSWE', columnspan=4)

label_nv = tk.Label(text="Qual o Nível do Pokémon")
label_nv.grid(row=5, column=0, padx=10, pady=10, sticky='NSWE', columnspan=4)

entry_nv = tk.Entry()
entry_nv.grid(row=6, column=0, padx=10, pady=10, sticky='NSWE', columnspan=4)

label_tipo = tk.Label(text="Qual o Tipo do Pokémon")
label_tipo.grid(row=7, column=0, padx=10, pady=10, sticky='NSWE', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=7, column=2, padx=10, pady=10, sticky='NSWE', columnspan=2)

botao_criar_codigo = tk.Button(text="Guardar", command=inserir_codigo)
botao_criar_codigo.grid(row=10, column=0, padx=10, pady=10, sticky='NSWE', columnspan=4)

janela.mainloop()

novo_pokemon = pd.DataFrame(
    lista_codigos,
    columns=['Nome', 'Tipo', 'Nível', 'Data']
)

pokemons = pd.concat([pokemons, novo_pokemon], ignore_index=True)

pokemons.to_excel(
    'f:/DaLucas_Codes/JANELINHAS/Pokemons.xlsx',
    index=False
)

print("Pokémons guardados com sucesso!")
