
cpf = input("Digite o cpf: ")
nome = input("Digite o nome: ")
idade = input("Digite o idade: ")

def cadastro_cliente():
    cadastroCliente = (f"{cpf}, {nome}, {idade}")
    file = open("ClienteCadastro.txt")
    file.append(cadastroCliente)


cadastro_cliente()


    #
    # cadastroCliente = ""
    # cadastroCliente.append([cpf, nome, idade])
    # print(cadastroCliente)
    # cadastroCliente = (f"{cpf}, {nome}, {idade}")
    # print(cadastroCliente)