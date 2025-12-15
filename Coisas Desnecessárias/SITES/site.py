from flask import Flask, render_template

# Criando a aplicação Flask
# Aqui eu digo para o Flask que meus templates estão na pasta "templates"
app = Flask(__name__, template_folder="template")

# Rota da página inicial
@app.route("/")
def homepage():
    # Renderiza o arquivo homepage.html dentro da pasta templates
    return render_template("homepage.html")

# Rota da página de contatos
@app.route("/contatos")
def contatos():
    # Renderiza o arquivo contatos.html
    return render_template("contatos.html")

# Rota para exibir um usuário específico pela URL
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    # Passo o nome do usuário para o template usuários.html
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
