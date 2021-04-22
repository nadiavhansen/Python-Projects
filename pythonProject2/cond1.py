# isinstance(x, int)
x = int(input('Digite um número inteiro: '))
if isinstance(x, int):
   print('ok')
else:
    raise Exception("Não é um número inteiro.")