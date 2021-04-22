file = open("teste.txt", "r")

with open("teste.txt") as file:
    arquivo = []
    for i in file:
        arquivo.append(i.strip())

print(arquivo)
print(arquivo[0].split(","))

# Deletar arquivo

# import os #importar biblioteca os
# os.remove("teste.txt")


# file_64 = open("texto_b64.txt", "r")
# file_to_save = open("teste_novo.txt", "a")
#
# for line in file_64:
#     file_to_save.write(line)