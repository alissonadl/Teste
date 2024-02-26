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