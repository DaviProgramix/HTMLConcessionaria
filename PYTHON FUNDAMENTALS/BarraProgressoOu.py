from tqdm import tqdm
import time
import requests

# Passo 1: Pegar a lista de CEPs
with open(r"F:\DaLucas_Codes\PYTHON FUNDAMENTALS\ceps.txt", "r") as arquivo:
    ceps = arquivo.read().splitlines()  # já quebra por linha

# Passo 2 e 3: Buscar informações de cada CEP e filtrar por Rio de Janeiro
enderecos = []

for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
    try:
        requisicao = requests.get(link)
        resposta = requisicao.json()
        cidade = resposta.get('city', '')
        bairro = resposta.get('district', '')

        if cidade.lower() == "rio de janeiro":
            enderecos.append((cep, bairro))
    except Exception as e:
        print(f"Erro com o CEP {cep}: {e}")
    
    time.sleep(0.2)  # evita sobrecarga na API

# Passo 4: Printar resultados
print(enderecos)
