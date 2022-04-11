# Baralho = coleçao de cartas (lista de cartas)
from random import randrange
from Carta import Carta
from PilhaEncadeada import Pilha, PilhaException


class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Baralho:
    # este construtor cria um baralho
    def __init__(self, criarVazio = None):
        if (criarVazio == True):
            # caso o parametro criarVazio seja passado como true, cria um baralho com a pilha vazia
            self.baralho = Pilha()
        else:
            self.baralho = Pilha() #atributo não obrigatorio do baralho
            naipe = ["Ouro", "Espada", "Paus", "Copas"]
            cor = ["vermelho", "preto", "preto", "vermelho"]
            numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]
            
            for idx in range(len(naipe)):

                for id in numeracao:
                    self.baralho.empilha(Carta(id, naipe[idx], cor[idx]))

    def __len__(self):
        # utilizamos o metodo tamanho no lugar do len para obter tamanho da pilha
        # len pegava o tamanho do array 
        return self.baralho.tamanho()

    def temCarta(self):
        if self.baralho.tamanho() > 0:
            return True
        else:
            return False

    def retirarCarta(self) -> Carta: 
        # utilizamos o metodo desempilha para retirar a ultima carta da pilha
        # antes estava pop() que retira o ultimo elemento de um array, mas nao de uma pilha
        try:
            return self.baralho.desempilha()
        except PilhaException:
            raise BaralhoException('O baralho está vazio. Não há cartas para retirar')

    def embaralhar(self):
        # esse metodo retira pega um numero aleatorio do baralho, retira a carta desta posicao e empilha novamente (repete esse processo na quantidadee de carta do baralho)
        for i in range(1, 52):
            posicao = randrange(1, 52)
            carta = self.baralho.removeElemento(posicao)
            self.baralho.empilha(carta)

    def empilharMonte(self, monteOrigem: Pilha, inicio, fim):
        # esse metodo empilha um monte (pilha) informado no parametro no baralho com base no inicio e fim
        contador = 1
        while(contador <= fim):
            if contador >= inicio:
                elemento = monteOrigem.elemento(contador)
                self.baralho.empilha(elemento)
            contador += 1

    def __str__(self):
        #foi removido o for que printava o array, agora apenas chamamos o _str_ da pilha
        return self.baralho.__str__() 



#tivemos que adaptar todos os metodos que antes utilizava o sel.baralho como array, para agora funcionar como uma pilha
