from collections import Counter
from Txt import Txt




class Sum(Txt):


    def sum_character(self):
        aparicoes = Counter(self.texto.lower())
        sum_chatacter = sum(aparicoes.values())
        return sum_chatacter


    def sum_character_sem_espaco(self):
        aparicoes = Counter(self.texto.lower())
        del aparicoes [' ']
        sum_character_sem_espaco = sum(aparicoes.values())
        return sum_character_sem_espaco

    def sum_palavras(self):
        aparicoes_palavras = self.texto.split()
        sum_palavras = len(aparicoes_palavras)
        return sum_palavras

    def format_sum(self):
        return f'Total de caracteres: {self.sum_character()} \n'\
               f'Total de caracteres sem espaço: {self.sum_character_sem_espaco()}\n' \
               f'Total de palavras: {self.sum_palavras()}\n'




