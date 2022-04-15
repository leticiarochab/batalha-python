from typing import List
from Jogador import Jogador
from Carta import Carta
from time import sleep

class Batalha:

    def __init__(self, jogador1: Jogador, jogador2: Jogador, limiteRodadas):
        self._jogador1 = jogador1
        self._jogador2 = jogador2
        self._qtdRodadas = 0
        self._temVencedor = False
        self._vencedor: Jogador = None
        self._limiteJogadas = limiteRodadas 

    def jogarRodada(self):
        self._qtdRodadas += 1
        print("\n\n ---------- Jogada [" + str(self._qtdRodadas) + "] ----------\n")
        temVencedorRodada = False
        cartasRodada = list()

        while(not temVencedorRodada):
            carta1 = self._jogador1._baralho.retirarCarta()
            sleep(1)
            print('Jogador [' + self._jogador1._nome + '] retirou a carta : ', carta1)
            carta2 = self._jogador2._baralho.retirarCarta()
            sleep(1)
            print('Jogador [' + self._jogador2._nome + '] retirou a carta : ', carta2)
            cartasRodada.append(carta1)
            cartasRodada.append(carta2)

            sleep(1)
            print("\n ** Checando resultado... **\n")
            if carta1.valorNumerico() > carta2.valorNumerico():
                sleep(1)
                print('Jogador ' + self._jogador1._nome + ' venceu a rodada')
                self.inserirCartasParaVencedor(self._jogador1, cartasRodada)
                self.temPerdedor(self._jogador2, self._jogador1)
                temVencedorRodada=True
            elif carta1.valorNumerico() < carta2.valorNumerico():
                sleep(1)
                print('Jogador ' + self._jogador2._nome + ' venceu a rodada')
                self.inserirCartasParaVencedor(self._jogador2, cartasRodada)
                self.temPerdedor(self._jogador1, self._jogador2)
                temVencedorRodada=True
            else:
                sleep(1)
                print('Empate na rodada')
                continue

    def temVencedorBatalha(self):
        if self._qtdRodadas+1 > self._limiteJogadas:
            if self._jogador1._baralho.__len__() > self._jogador2._baralho.__len__():
                self._vencedor = self._jogador1
            elif self._jogador2._baralho.__len__() > self._jogador1._baralho.__len__():
                self._vencedor = self._jogador2
            else:
                self._vencedor = None
            return True
        elif not self._jogador1._baralho.temCarta():
            self._vencedor = self._jogador1
            return True
        elif not self._jogador2._baralho.temCarta():
            self._vencedor = self._jogador2
            return True
        else:
            return False
        


    def temPerdedor(self, perdedorRodada: Jogador, vencedorRodada: Jogador):
        sleep(1)
        print('\nO jogador '      + perdedorRodada._nome 
                                + ' perdeu a rodada e restam ' 
                                + str(perdedorRodada._baralho.__len__()) + ' cartas')

        if not perdedorRodada._baralho.temCarta():
            self._temVencedor = True
            self._vencedor = vencedorRodada

    def inserirCartasParaVencedor(self, jogador: Jogador, lista: List[Carta]):
        sleep(1)
        print('\nO vencedor receberá as cartas: ')
        for carta in lista:
            print(carta)
            jogador._baralho.baralho.inserirNaBase(carta)

        sleep(1)
        print('\nO jogador '  + jogador._nome 
                            + ' ficou com ' 
                            + str(jogador._baralho.__len__()) + ' cartas')
        

        