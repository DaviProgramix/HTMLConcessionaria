print("Seja Bem-Vindo ao Comprinhas Web.")

listaComprinhas = ["Arroz", "Feijão", "Batata Frita", "Carne Moida", "Massa de Lasanha"]
itensComprados = []

press = input("Para continuar pressione 1: ")

if press == "1":
    while True:
        objeto = input("Digite o que deseja comprar: ").lower()

        lista_normalizada = [item.lower() for item in listaComprinhas]

        if objeto in lista_normalizada:
            print("Esse item já foi adicionado na lista de compras.")
        else:
            print("Item não encontrado.")

        itensComprados.append(objeto)

        continuar = input("Quer adicionar mais algum item? (s/n): ").lower()
        if continuar != "s":
            break
else:
    print("Pressione 1 novamente.")

print(f"Seus itens são: {itensComprados}")
