# 2 – Receba quatro palavras. Todas as palavras devem ser mostradas no final em uma única String.
# Regras:
# Todas as letras devem estar em maiúscula
# Todas as palavras na string final devem terminar com !!!! join
# Os caracteres “a” ou “A” devem ser substituídos por @
# Qualquer outra vogal deve ser substituída por *

p1 = str(input("Digite uma palavra: "))
p2 = str(input("Digite outra palavra: "))
p3 = str(input("Digite outra palavra: "))
p4 = str(input("Digite outra palavra: "))

final = p1 + "!!!" + p2 + "!!!" + p3 + "!!!" + p4 + "!!!"
final = final.upper().replace("A", "@").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")
print(final.upper())

for palavra in range(4):
    p = str(input("Digite uma palavra: "))
    final = p(palavra)
    final = p.upper().replace("A", "@").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")
print(final)

