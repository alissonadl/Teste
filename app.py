from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo'

@app.route('/alunos')
def alunos():
    return render_template('alunos.html')

@app.route('/professores')
def professores():
    return render_template('professores.html')

@app.route('/contato')
def contato():
    telefone = '1234-5678'
    email = 'alisson@ifrn.com.br'
    return render_template('contato.html', x=email, tel=telefone)

@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome = nome)