from collections import Counter

from Txt import Txt

class AnalyticalWord(Txt):




    def word_frequency(self):
        aparicoes = Counter(self.texto.split())
        vezes_aparece = aparicoes.most_common(10)
        return vezes_aparece

    def word_frequency_proportion(self):
        aparicoes = Counter(self.texto.split())
        total_palavras = sum(aparicoes.values())
        proporcao = [(palavra, freuqnecia / total_palavras) for palavra, freuqnecia in aparicoes.items()]
        proporcao = Counter(dict(proporcao))
        mais_comuns = proporcao.most_common(5)
        return mais_comuns




