from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def PaginaInicial():
    return render_template("PaginaInicial.html")

@app.route("/Login")
def Login():
    return render_template("Login.html")

# A rota Usuarios precisa aceitar POST
@app.route("/Usuarios", methods=["POST"])
def usuarios():
    # Captura os dados do formulário
    usuario = request.form.get("usuario")
    email = request.form.get("email")
    senha = request.form.get("senha")
    idade = request.form.get("idade")
    
    # Passa os dados para a página de usuários
    return render_template("Usuarios.html", usuario=usuario, email=email, senha=senha, idade=idade)

if __name__ == "__main__":
    app.run(debug=True)
