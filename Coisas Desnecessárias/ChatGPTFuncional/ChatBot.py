from openai import OpenAI

client = OpenAI()

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
        )

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages = lista_mensagens,
    )
    
    return resposta.choices[0].message.content

lista_mensagens = []
while True:
    texto = input("Escreva aqui sua mensagem: ")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print("ChatBot:", resposta)
