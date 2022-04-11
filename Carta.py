class Carta:

    def __init__(self, numero, naipe, cor):
        self.__numero = numero
        self.__naipe = naipe

    @property
    def naipe(self):
        return self.__naipe

    @property
    def numero(self):
        return self.__numero

    def valorNumerico(self):
        if self.__numero == 'valete':
            return 11
        elif self.__numero == 'dama':
            return 12
        elif self.__numero == 'rei':
            return 13
        elif self.__numero == 'As':
            return 14
        else:
            return int(self.__numero)

    def __str__(self):  # todas as informacoes da carta
        return f'{self.__numero} de {self.__naipe}'