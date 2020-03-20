from collections import Counter

from Txt import Txt

class AnalyticalCharacteres(Txt):


    def __str__(self):
        return self.format()

    def character_frequency(self):
        aparicoes = Counter(self._texto.lower())
        vezes_aparece = aparicoes.most_common(10)
        return vezes_aparece




    def character_frequency_proportion(self):

        aparicoes = Counter(self._texto.lower())
        total_de_caracteres = sum(aparicoes.values())
        proporcoes = [(letra, frquencia / total_de_caracteres) for letra, frquencia in aparicoes.items()]
        proporcoes = Counter(dict(proporcoes))
        mais_comuns = proporcoes.most_common(10)
        for caractere, proporcao in mais_comuns:
            return caractere, proporcao 
            #print ('Caractere: {} => {:.2f}%'.format(caractere,proporcao *100))

    def format(self):

            return f'{self.character_frequency()}\n' \
                   f'{self.character_frequency_proportion()}\n'



