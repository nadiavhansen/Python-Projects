# class Jogador():

def selecionar_carta(self, mao_de_cartas):
    carta_selecionada = int(input('\nSelecione a carta desejada: '))
    carta_selecionada = mao_de_cartas[carta_selecionada]
    mao_de_cartas.remove(carta_selecionada)
    print(f'A carta selecionada foi: {carta_selecionada}\n')
    return carta_selecionada, mao_de_cartas