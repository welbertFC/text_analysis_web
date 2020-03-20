from collections import Counter

from Txt import Txt

class AnalyticalCharacteres(Txt):




    def character_frequency(self):
        aparicoes = Counter(self._texto.lower())
        vezes_aparece = aparicoes.most_common(10)
        return vezes_aparece




    def character_frequency_proportion(self):

        aparicoes = Counter(self._texto.lower())
        total_de_caracteres = sum(aparicoes.values())
        proporcoes = [(letra, frquencia / total_de_caracteres) for letra, frquencia in aparicoes.items()]
        proporcoes = Counter(dict(proporcoes))
        mais_comuns = proporcoes.most_common(5)
        return mais_comuns






