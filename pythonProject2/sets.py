my_set = {"Aula1", "Aula2", "Banana"} #são distribuídos aleatoriamente, são imutáveis (pode adicionar ou excluir apenas)
my_set.add("Maçã")
my_set.remove("Aula2") #retorna erro se não exstir
my_set.discard("Aula2") #não retorna erro se não existir, ele apenas ignora
my_set.pop() #descarta a última posição do set, sem saber qual será
print(my_set)

set2 = {"Teste"}
my_set.update(set2) #vai adicionar, sem duplicar iguais
set3 = my_set.union(set2) #cria uma cópia
print(my_set)

my_set.clear() #limpa o set
print(my_set)

del my_set #deleta o set da memória

print(set3)
