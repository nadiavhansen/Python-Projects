from Jogo import *
from Jogador import *
from Computador import *


def jogar():

    jogo = Jogo()

    jogador = Jogador()
    computador = Computador()
    round_atual = Jogo.Round()

    cartas_jogador = jogo.distribuir_cartas()
    print(f'\nAs suas cartas são: \n{cartas_jogador}')
    mao_de_cartas = cartas_jogador
    carta_selecionada = jogador.selecionar_carta(cartas_jogador)
    print('-='*15)

    carta_computador = computador.jogadas_computador()
    print(f'\nComputador: {carta_computador}\n')
    print('-='*15)
    # round_atual.vencedor_do_round(carta_computador, carta_selecionada)

    for i in range(len(mao_de_cartas)):
        if round_atual.vencedor_do_round(carta_computador, carta_selecionada) != 'Venceu o round!':
            print('...Tente novamente!')
            print(f'\nAs cartas restantes são: {mao_de_cartas}')
            carta_selecionada = jogador.selecionar_carta(cartas_jogador)
            print('-=' * 15)
            carta_computador = computador.jogadas_computador()
            print(f'\nComputador: {carta_computador}\n')
            print('-=' * 15)
            if len(mao_de_cartas) == 0:
                if round_atual.vencedor_do_round(carta_computador, carta_selecionada) != 'Venceu o round!':
                    print('Não foi dessa vez... Mas não desanime, jogue de novo!')
                else:
                    pass
                    print('Venceu o jogo!!!')
        else:
            print('Venceu o jogo!!!')
            break

jogar()