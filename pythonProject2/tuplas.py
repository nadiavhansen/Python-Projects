# lista []
# tupla ()
# set {}
# dicionario {:}

# scalar = [1]
# vetor = [1, 2]
# matriz = [[1, 2], [3, 4]]
# tensor = []

# y = "A", "A" retorna uma tupla
# x, z = y

tupla = (1, 2, 3) #feita por parenteses
tupla2 = (1,) #se for um item, deve ser colocada a vírgula para não ser uma variavel inteira ao invés de tupla
tupla3 = () #apenas parenteses é uma tupla vazia
tupla4 = tupla + tupla2
tupla4 += tupla3

print(tupla[0])
print(type(tupla2))
print(len(tupla))
print(tupla4)

print("")

print(tupla)
lista = list(tupla)
lista.append(3)
tupla = tuple(lista)
print(tupla)
