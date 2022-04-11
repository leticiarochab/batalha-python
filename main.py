from Baralho import Baralho
from Jogador import Jogador
from Batalha import Batalha
from time import sleep

def mostrarMenu():
    print("[1] - Jogar uma partida")
    print("[0] - Sair do jogo")
    op = int(input("\nDigite uma opção: "))
    return op

print("\n")
print("*******************************")
print("*                             *")
print("*      BEM VINDO AO JOGO      *")
print("*                             *")
print("*******************************")
print("\n")

op = 999
while(op != 0):
    op = mostrarMenu()

    if op == 1:
        print("\n---------------------------------\n")
        nomeJogador1 = input("Informe o nome do jogador 1: ")
        nomeJogador2 = input("Informe o nome do jogador 2: ")
        qtdLimite    = int(input("Informe a quantidade limite de rodadas: "))

        print("\n *** PREPARANDO PARTIDA... \n")

        # criar baralho completo
        baralho = Baralho()
        sleep(0.8)
        print("1 - BARALHO CRIADO")

        # embaralhar baralho completo
        baralho.embaralhar()
        sleep(0.8)
        print("2 - O BARALHO FOI EMBARALHADO")

        # criar os 2 jogadores com baralho vazio
        jogador1 = Jogador(nomeJogador1, Baralho(criarVazio=True))
        jogador2 = Jogador(nomeJogador2, Baralho(criarVazio=True))

        sleep(0.8)
        print("3 - JOGADORES CRIADOS")
        print("*** Jogador 1 - ", jogador1._nome)
        print("*** Jogador 2 - ", jogador2._nome)

        # empilhamos metade do baralho completo em cada jogador
        jogador1._baralho.empilharMonte(baralho.baralho, 1, 26)
        jogador2._baralho.empilharMonte(baralho.baralho, 27, 52)
        sleep(0.8)
        print("4 - CADA JOGADOR RECEBEU 26 CARTAS")

        sleep(0.8)
        print("\n******* A BATALHA SERÁ INICIADA *******")
        # criar batalha passando os dois jogadores
        batalha = Batalha(jogador1, jogador2, qtdLimite)

        # enquanto ninguem vencer, continua jogando
        while(not batalha.temVencedorBatalha()):
            batalha.jogarRodada()

        # aqui, temos um vencedor ou empate
        if batalha._vencedor == None:
            sleep(1)
            print('\n** A BATALHA TERMINOU EMPATADA **\n')
        else:
            sleep(1) 
            print('\n** VENCEDOR DA PARTIDA: ' + batalha._vencedor._nome)
            print("------------------------------------\n")
            
print("\nJOGO ENCERRADO\n")


























