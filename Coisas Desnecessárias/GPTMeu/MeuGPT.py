import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    if "python" in message.content.lower():
        resposta = "Parabéns, está aprendendo uma boa linguagem"
    else:
        resposta = "Já pensou em aprender Python?"

    await cl.send_message(resposta)
