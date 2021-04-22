# 3 – Receba uma String, após isso, veja letra por letra e avance as consoantes, 9 letras para frente
# (Ex: “g” vira “o”) e as vogais 4 letras para trás (Ex: “e” vira “a”)
# Caso o avanço ultrapasse “z”, continue no “a”.
# Caso o regresso ultrapasse o “a”, continue no “z”
# Ex: “Ara” vira “waw”


import string

lower_letters = string.ascii_lowercase #alfabeto minusculo
palavra = input("Digite uma palavra: ")
vogais = "aeiou" # "aeiou" é igual a ["a", "e", "i", "o", "u") pois uma string é um array

nova_palavra = ""

for i in palavra:
    if i.lower() in vogais:
        index = lower_letters.index(i.lower()) - 4
        nova_palavra += lower_letters[index]
    else:
        index = lower_letters.index(i.lower()) + 9

        # verdadeiro if condição else falso
        novo_index = index if index < 26 else index - 26

        nova_palavra += lower_letters[novo_index]

print(nova_palavra)
print(string.ascii_lowercase)






