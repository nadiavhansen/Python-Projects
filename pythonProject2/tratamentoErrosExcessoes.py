try:
    print(10 / 0)
except:
    print("Não é possível dividir por zero!")


try:
    lista = [1, 2]
    lista[5]
except:
    pass


try:
    lista = [1, 2, 3]
    lista[5]
except IndexError:
    print("Index error")
except ArithmeticError:
    print("Arithmetic error")

