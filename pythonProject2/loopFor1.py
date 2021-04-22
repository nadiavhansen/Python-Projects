# 1 - Criar um “Torneio entre números”. Receba vários números, eles devem “lutar” entre seus pares e o maior ficar.
# Ex:
# Recebo: [5, 9, 3, 5, 2, 1, 6, 3]
# Primeiro round = [9, 5, 2, 6]
# Segundo round = [9, 6]
# Terceiro round = [9]
# 9 é vencedor
# Caso o número de competidores no round seja ímpar, o último passará de round direto.
# Caso os competidores empatem, os dois perdem.

# lista = []
# vezes = int(input("Digte quantas vezes vai rodar"))
#
# for i in range(vezes):
#     lista.append(int(input("Número: ")))
# print(lista)
#
# round2 = []
# if (len(lista)+1) % 2 == 0:
#     round2.append(lista[-1])
#
# if lista[0] > lista[1]:
#     round2.append(lista[0])
# else:
#     round2.append(lista[1])
#
# if lista[2] > lista[3]:
#     round2.append(lista[2])
# else:
#     round2.append(lista[3])
# print(round2)
#
#
# round3 = []
# if (len(round2)+1) % 2 == 0:
#     round3.append(round2[-1])
#
# if lista[0] > lista[1]:
#     round3.append(round2[0])
# else:
#     round3.append(round2[1])
# print(round3)


# x = max([1, 4])
# x é igual a 4
# min([2, 3])


lutadores = []

for i in range(int(input("Quantas vezes quer rodar?\n"))):
    lutadores.append(int(input("Novo número: ")))

proximo_round = lutadores.copy()

while len(proximo_round) > 1:

    round_atual = proximo_round.copy()

    if len(round_atual) % 2 == 1:
        round_atual.append(0) #adiciona o numero 0 no final
    proximo_round.clear()

    for i in range(len(round_atual)):

        if i % 2 == 0:
            if round_atual[i] != round_atual[i+1]:
             vencedor = max(round_atual[i], round_atual[i+1])
             proximo_round.append(vencedor)

        else:
            pass

print(proximo_round)







