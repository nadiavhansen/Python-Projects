import random

class Jogo():

    print('PEDRA, PAPEL, TESOURA!')


    def distribuir_cartas(self):

        cartas_sorteadas = [random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)]

        return cartas_sorteadas


class Jogador():

    def selecionar_carta(self, mao_de_cartas):
        carta_selecionada = int(input('\nSelecione a carta desejada: '))
        carta_selecionada = mao_de_cartas[carta_selecionada]
        mao_de_cartas.remove(carta_selecionada)
        print('A carta selecionada foi', carta_selecionada)
        return carta_selecionada

class Computador():

    def jogadas_computador(self):

        jogada_computador = random.randint(1, 3)
        return jogada_computador


class Round(Jogo):


    def vencedor_do_round(self, carta_computador, carta_selecionada):

        resultado = ''

        for i in range(len(self.distribuir_cartas())):
            if carta_computador == 1:
                if carta_selecionada == 1:
                    resultado = 'Empate'
                elif carta_selecionada == 2:
                    resultado = 'Venceu'
                    pass
                elif carta_selecionada == 3:
                    resultado = 'Perdeu'
            if carta_computador == 2:
                if carta_selecionada == 1:
                    resultado = 'Perdeu'
                elif carta_selecionada == 2:
                    resultado = 'Empate'
                elif carta_selecionada == 3:
                    resultado = 'Venceu'
                    pass
            if carta_computador == 3:
                if carta_selecionada == 1:
                    resultado = 'Venceu'
                    pass
                elif carta_selecionada == 2:
                    resultado = 'Perdeu'
                elif carta_selecionada == 3:
                    resultado = 'Empate'
        print(resultado)


        return resultado


jogo = Jogo()

jogador = Jogador()
cartas_jogador = jogo.distribuir_cartas()
print('\nAs suas cartas são: ')
print(cartas_jogador)
carta_selecionada = jogador.selecionar_carta(cartas_jogador)

computador = Computador()
carta_computador = computador.jogadas_computador()
print('\nComputador selecionou', carta_computador)

round_atual = Round()
round_atual.vencedor_do_round(carta_computador, carta_selecionada)



print("")
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
