import wikipedia

wikipedia.set_lang("pt")

buscas = wikipedia.search("Império Romano")
print(buscas)

pagina = wikipedia.page(buscas[0])
resumo = pagina.summary
conteudo = pagina.content
imagens = pagina.images

print(conteudo)
print("#" * 10)
print(resumo)
print("#" * 10)
print(imagens)


