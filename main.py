from flask import Flask, render_template, request, redirect, url_for
from Txt import Txt
import Sum
import Analytical_characters
import  Analytical_word

app = Flask(__name__)
app.secret_key = 'senha'

class Analise_caracteres():
    def __init__(self, caracteres, vezes_que_aparece):
        self.caracteres = caracteres
        self.vezes_que_aparece = vezes_que_aparece

class Frequencia_caracteres():
    def __init__(self, caractere, proporcao):
        self.caractere = caractere
        self.proporcao = proporcao

class Word_frequency():
    def __init__(self, palavra, vezes_que_palavra_aparece):
        self.palavra = palavra
        self.vezes_que_palavra_aparece = vezes_que_palavra_aparece
class Word_frequency_proportion():
    def __init__(self, palavra, proporcao):
        self.palavra = palavra
        self.proporcao = proporcao



analise_caracteres = []
frequencia_caracteres = []
word_frequency_list = []
word_frequency_proportion_list = []

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
                           fequencia=analise_caracteres,
                           proporcao = frequencia_caracteres,
                           analise_palavra = word_frequency_list,
                           proporcao_palavra = word_frequency_proportion_list)


@app.route('/analise_caractere', methods=['POST', ])
def analise_caractere():
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
        analise_caracteres.append(analise)

    #anlise de proporcão de caracteres
    character_frequency_proportion = Analytical_characters.AnalyticalCharacteres.character_frequency_proportion(objeto_texto)
    for caracteres, proporcao in character_frequency_proportion:
        analise_proporcao = Frequencia_caracteres(caracteres,proporcao * 100)
        frequencia_caracteres.append(analise_proporcao)

    #anlise de frequencia de palavras
    word_frequency = Analytical_word.AnalyticalWord.word_frequency(objeto_texto)
    for palavra, vezes_que_palavra_aparece in word_frequency:
        analise_palavra = Word_frequency(palavra,vezes_que_palavra_aparece)
        word_frequency_list.append(analise_palavra)

    #anlise de proporção de palavras
    word_frequency_proportion = Analytical_word.AnalyticalWord.word_frequency_proportion(objeto_texto)
    for palavra, proporcao_palavra in word_frequency_proportion:
        analise_proporcao_palavra = Word_frequency_proportion(palavra,proporcao_palavra * 100)
        word_frequency_proportion_list.append(analise_proporcao_palavra)






    return redirect(url_for('resposta', character_sem_espaco=character_sem_espaco,
                            sum_character=sum_character,
                            sum_palavras=sum_palavras))





app.run()
