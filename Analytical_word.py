from collections import Counter

from Txt import Txt

class AnalyticalWord(Txt):


    def __str__(self):
        return self.format()

    def word_frequency(self):
        aparicoes = Counter(self.texto.split())
        vezes_aparece = aparicoes.most_common()
        for palavra, vezes_que_aparece in vezes_aparece:
            print(f'palavra: {palavra} == {vezes_que_aparece}')

    def word_frequency_proportion(self):
        aparicoes = Counter(self.texto.split())
        total_palavras = sum(aparicoes.values())
        proporcao = [(palavra, freuqnecia / total_palavras) for palavra, freuqnecia in aparicoes.items()]
        proporcao = Counter(dict(proporcao))
        mais_comuns = proporcao.most_common(15)
        for palavra, freuqnecia in mais_comuns:
            print("{} == {:.2f}%".format(palavra, freuqnecia *100))


    def format(self):

            return f'{self.word_frequency()}\n' \
                   f'{self.word_frequency_proportion()}\n'


