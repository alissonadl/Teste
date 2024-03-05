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

'''
#Colocando valor "anonimo" como valor padrão.

@app.route('/usuario')
@app.route('/usuario/')
@app.route('/usuario/<nome>')
def usuario(nome='anonimo'):
    return render_template('usuario.html', nome = nome)
'''

#Forma alternativa e "correta" de definir valores padrão sem que o usuário passe.
''
@app.route('/usuario', defaults={"nome":"anônimo"})
@app.route('/usuario/', defaults={"nome":"anônimo"})
@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome = nome)
#'''

''
@app.route('/dobro/<int:n>')
def dobro(n):
    calculo = 2 * n
    return 'O valor dobrado é: '+str(calculo)
#'''

#Colocando valores padrão inteiros
@app.route('/dobrod/<int:n>')
def dobrod(n):
    calculod = 2 * n
    return 'O valor dobrado é: ' + str(calculod)