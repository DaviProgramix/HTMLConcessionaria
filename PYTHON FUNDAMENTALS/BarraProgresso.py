from tqdm import tqdm
import time

# Forma Mais Simples De Criar Uma Barra De Progresso
#for i in tqdm(range(10)):
    #time.sleep(1)

#lista = [1, 2, 3, 10, 15]

#for item in tqdm(lista):
    #time.sleep(1)

#with tqdm(total=100) as barra_progresso:
    #for i in range(10):
        #time.sleep(1)
        #barra_progresso.update(1)

# Quero Entregar Para Cidade De Rio De Janeio
import requests


# Passo 1 Pegar A Lista De Ceps
with open(r"F:/DaLucas_Codes/PYTHON FUNDAMENTALS/ceps.txt", "r") as arquivo:
    ceps = arquivo.read()
ceps = ceps.split("\n")
# Passo 2 Pegar As Informações De Cada Cep
enderecos = []
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'

    # Passo 3 Verificar Se a Cidade É Rio De Janeiro
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
# Passo 4 Printar O Cep E O Bairro
    if cidade == "Rio de Janeiro":
        enderecos.append((cep, bairro))

print(enderecos)