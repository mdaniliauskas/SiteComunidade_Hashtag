from flask import Flask, render_template
from forms import FormLogin, FormCriarConta
app = Flask(__name__)

app.config['SECRET_KEY'] = '1234' # Teste, depois configurar corretamente

lista_usuarios = [
    "Ana Souza",
    "Carlos Lima",
    "Fernanda Alves",
    "João Pedro",
    "Mariana Silva",
    "Lucas Rocha",
    "Patrícia Gomes",
    "Rafael Costa",
    "Beatriz Ramos",
    "Eduardo Pinto"
]

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login')
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)

if __name__ == "__main__":
    app.run(debug=True)

