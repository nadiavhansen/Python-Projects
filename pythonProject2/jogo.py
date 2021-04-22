import random

class Jogo:
    print('-='*15)
    print('PEDRA, PAPEL, TESOURA!')

    print('Opções: '
                '\n1 - Pedra'
                '\n2 - Papel'
                '\n3 - Tesoura')
    print('-='*15)

    def distribuir_cartas(self):

        cartas_sorteadas = [random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)]

        return cartas_sorteadas


class Jogador():

    def selecionar_carta(self, mao_de_cartas):

        while True:
            try:
                carta_selecionada = int(input('\nSelecione a carta desejada: '))
                carta_selecionada = mao_de_cartas[carta_selecionada]
                mao_de_cartas.remove(carta_selecionada)
            except:
                pass
            print(f'A carta selecionada foi: {carta_selecionada}\n')
            return carta_selecionada, mao_de_cartas


class Computador():

    def jogadas_computador(self):

        jogada_computador = random.randint(1, 3)
        return jogada_computador


class Round():

    def vencedor_do_round(self, carta_computador, carta_selecionada):

        carta_selecionada = carta_selecionada[0]

        if carta_computador == 1:
            if carta_selecionada == 1:
                resultado = 'Empatou o round...'
            elif carta_selecionada == 2:
                resultado = 'Venceu o round!'
            elif carta_selecionada == 3:
                resultado = 'Perdeu o round...'
            print(resultado)
        if carta_computador == 2:
            if carta_selecionada == 1:
                resultado = 'Perdeu o round...'
            elif carta_selecionada == 2:
                resultado = 'Empatou o round...'
            elif carta_selecionada == 3:
                resultado = 'Venceu o round!'
            print(resultado)
        if carta_computador == 3:
            if carta_selecionada == 1:
                resultado = 'Venceu o round!'
            elif carta_selecionada == 2:
                resultado = 'Perdeu o round...'
            elif carta_selecionada == 3:
                resultado = 'Empatou o round...'
            print(resultado)
        return resultado


def jogar():

    jogo = Jogo()

    jogador = Jogador()
    computador = Computador()
    round_atual = Round()

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

# jogada.jogador()

# jogada.resultado_da_jogada()


# carta = int(input('Opções: '
#                      '\n1 - Pedra'
#                      '\n2 - Papel'
#                      '\n3 - Tesoura'))


# def ver_cartas(self, cartas):
#
#     cartas_jogador = self.distribuir_cartas()
#     print(cartas_jogador)
#     return cartas_jogador

#
#         carta_sorteada_1 = cartas_sorteadas[0]
#         carta_sorteada_2 = cartas_sorteadas[1]
#         carta_sorteada_3 = cartas_sorteadas[2]
