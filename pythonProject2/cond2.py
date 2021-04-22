n = int(input("Digite um número de 0 a 100: "))
if n < 50: print('Está okay')
elif n < 75: print('Ta complicado')
else: print('Ta dificil')

print("Está ok") if n < 50 else print("Ta complicado") if n < 75 else print("Ta difiil")