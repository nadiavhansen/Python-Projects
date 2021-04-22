import random

#class Jogo():
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

#class Round():

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