#dicionario serve para mapeamento

# keys()
# values()
# items


dicio = {"chave" : "valor"} #chave pode ser inteiro ou string, valor pode ser qualquer objeto
print(dicio["chave"]) #imprime o valor

dicio = {"chave" : "valor", "chave1" : "valor1"}
# print(dicio.keys())
# print(dicio.values())
# print(dicio.items())
# print(list(dicio.items()))

dicio2 = {"nova":2}
dicio["chave"] = "maçã"
print(dicio)

for i in dicio:
    print(i)