class Animais: # Super classe, não instancie

    rabo = True
    patas = 0
    ordem = ""

    def printar(self):
        print('Oiii')

class Mamalia():

    mamas = True

class Gato(Mamalia, Animais):
    #rabo não é necessário, pq continua True
    patas = 4 #polimorfismo, alterar o atributo
    ordem = "Mamalia" #polimorfismo, alterar o atributo

    def printar(self):
        return True #aqui está sobrescrevendo na funcao printar da mãe

    def andar1(self):
        return self.patas

    # def andar2(self):
    #     return super(Mamalia, self).mamas

    def andar(self):
        return super(Gato, self).printar() #para acessar a classe anterior

    pass

# # tudo o que a classe mãe tem, a classe filha também tem
animal = Gato()
# print(animal.patas)
animal.andar()
print(animal.andar1())
# print(animal.andar2())



