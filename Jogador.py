from Baralho import Baralho


class Jogador: 

    def __init__(self, nome, baralho: Baralho):
        self._nome = nome
        self._baralho = baralho

    def __str__(self): 
        return self._nome