# string = "Teste"
#
# for i in string:
#     print(i)
# print("")
#
# for i in range(10):
#     print(i)
# print("")
#
# for i in range(10, 20):
#     print(i)
# print("")
#
# for i in range(10, 20, 2):
#     print(i)
# print("")
#
# for i in range (0,len(string)):
#     print(i)
# print("")
#
# lista = [1, "B", True]
# for i in range (0, len(lista)):
#     print(i)
#     print(lista[i])
#
# lista2 = [i for i in range(100)] #[o que vai ser adicionado, laço ,onde vai percorrer]
# print(lista2)

# for i in range(10):
#     i # se for quebrado (break) o loop não usa o else
# else:
#     del i #para deletar o laço quando acabar
#
#
# lista = [var for var in iteravel] tudo o que está antes do for é append
#
# #é igual a:
#
# lista = []
# for var in iteravel:
#     lista.append(var)



# letras = ["A", "B", "C"]
#
# lista = ["Essa é a letra " + i for i in letras] #append em cada i
# print(lista)
#


# numeros = [i for i in range(10)]
#
# pares = [num for num in numeros if num % 2 == 0]
#
# print(pares)


# lista = []
# for i in range(10):
#     if not i % 2 == 0:
#         continue
#     print(i)
#     lista.append(i)
# print(lista)


for i in range(10):
    print(i)
    if i > 5:
        break
