from flask import Flask, render_template, request, redirect, url_for

from Txt import Txt
import Sum


app = Flask(__name__)
app.secret_key = 'senha'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resposta' )
def resposta():
    sum_character = request.args.get('sum_character')
    character_sem_espaco = request.args.get('character_sem_espaco')
    sum_palavras = request.args.get('sum_palavras')

    return render_template('resposta.html',  sum_character = sum_character,
                           character_sem_espaco = character_sem_espaco,
                           sum_palavras = sum_palavras)

@app.route('/analise_soma', methods = ['POST',])
def analise_soma():
    texto = request.form['text']
    objeto_texto = Txt(texto)
    character_sem_espaco = Sum.Sum.sum_character_sem_espaco(objeto_texto)
    sum_character = Sum.Sum.sum_character(objeto_texto)
    sum_palavras = Sum.Sum.sum_palavras(objeto_texto)

    return redirect(url_for('resposta',character_sem_espaco = character_sem_espaco,
                            sum_character =  sum_character,
                            sum_palavras = sum_palavras))


app.run(debug=True)