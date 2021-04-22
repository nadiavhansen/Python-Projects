# class Teste:
#     # self só usa dentro da classe
#
#     idade = 8 #propriedade estatica, para manter a idade sempre a mesma (mas pode mudar depois)
#
#     def func(self): #funções dentro de classe são chamadas de métodos
#         self.nome = 'Nádia' #vira um atributo da classe, funciona como o this.
#
#     def salvar_dados(self, nome, idade, cpf):
#         #aqui serve para alterar os dados
#         self.nome = nome
#         self.idade = idade
#         self.cpf = cpf
#
#     def teste(self):
#         self.idade
#         print('Seu nome é ' + self.nome) #essa classe pega a variável nome
#
#     def func3(self):
#         self.teste() #self: nesta classe pega a função teste
#         pass


# variavel é = classe (instanciar)
# pessoa1 = Teste()

# print(type(pessoa1))
# print(pessoa1.idade)
# pessoa1.salvar_dados('Nadia', 25, "000")
# pessoa1.teste() #retorna 'Seu nome é Nadia'
# print(pessoa1.idade) #retorna nova idade 25

class Teste2:

    # def __init__(self, name, idade=None): #__nome__ é metodo magico #None para não ser obrigatorio atribuir valor
    #     # print('Testando')
    #     # print(nome,idade)
    #     self.name = name
    #     self.idade = idade

    # def __del__(self):
    #     print('Foi deletado com fracasso')

    # def __str__(self): #retorna string
    #     return f'{self.name}, {self.idade}'
    #     pass
    #
    def __add__(self, other):
        print('\nAdição')
        print(other)
        resultado = 10 + other
        print('Resultado', resultado)
        return resultado

    def __mul__(self, other):
        print('\nMultiplicacao')
        print(other)
        resultado = 10 * other
        print('Resultado', resultado)
        return resultado

    def __call__(self, *args, **kwargs):
        print('Printa isso', kwargs["nome"])


# # __del__
# pessoa2 = Teste2('Nadia', 25)
# # del pessoa2
# # input('AA')

# # __str__
# print(pessoa2)
# print(type(pessoa2.idade))

# # __add__
# numero = Teste2()
# print(numero + 6 + 9)

# #__mul__
# numero = Teste2()
# print(numero * 3 * 9)

# #__call__
# pessoa = Teste2()
# pessoa(nome='Gustavo') # ativa o método call




def funcao(nome): #parametro é o que pede
    pass
funcao("Nádia") #argumento é o que manda