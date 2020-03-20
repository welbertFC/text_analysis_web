from flask import Flask, render_template, request, redirect, url_for
from collections import Counter
from Txt import Txt
import Sum
import Analytical_characters

app = Flask(__name__)
app.secret_key = 'senha'

class Analise_caracteres():
    def __init__(self, caracteres, vezes_que_aparece):
        self.caracteres = caracteres
        self.vezes_que_aparece = vezes_que_aparece


caracteres = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resposta')
def resposta():
    sum_character = request.args.get('sum_character')
    character_sem_espaco = request.args.get('character_sem_espaco')
    sum_palavras = request.args.get('sum_palavras')



    return render_template('resposta.html', sum_character=sum_character,
                           character_sem_espaco=character_sem_espaco,
                           sum_palavras=sum_palavras,
                           fequencia=caracteres)


@app.route('/analise_soma', methods=['POST', ])
def analise_soma():
    #analise de soma
    texto = request.form['text']
    objeto_texto = Txt(texto)
    character_sem_espaco = Sum.Sum.sum_character_sem_espaco(objeto_texto)
    sum_character = Sum.Sum.sum_character(objeto_texto)
    sum_palavras = Sum.Sum.sum_palavras(objeto_texto)

    #anlise de frequencia de caracteres 
    character_frequency = Analytical_characters.AnalyticalCharacteres.character_frequency(objeto_texto)
    for caractere, vezes_que_aparece in character_frequency:
        analise = Analise_caracteres(caractere,vezes_que_aparece)
        caracteres.append(analise)


    return redirect(url_for('resposta', character_sem_espaco=character_sem_espaco,
                            sum_character=sum_character,
                            sum_palavras=sum_palavras))


app.run(debug=True)
