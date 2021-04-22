n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 % n2 == 0 and n1 % n3 == 0:
    print(True)
else:
    print(False)