# 2 – Crie algo que cadastre uma pessoa (Nome, idade, cpf).
# Crie algo que o usuário possa listar todas as pessoas cadastradas.
# Crie algo o usuário possa selecionar uma pessoa cadastrada pelo cpf.
# Crie algo em que o usuário possa altera algum dos dados de uma pessoa.
# Crie algo em que o usuário possa deletar alguma pessoa.

bancoDeDados = {
    "cpf" : {
        "nome": str(),
        "idade": int()
    }
}

def cadastroPessoas():
    cpfPessoa = input("Digite o cpf da pessoa: ")
    nomePessoa = input("Digite o nome da pessoa: ")
    idadePessoa = int(input("Digite a idade da pessoa: "))
    bancoDeDados[cpfPessoa] = {"nome": nomePessoa, "idade": idadePessoa}

def listarPessoas():
    print("Lista de pessoas cadastradas: CPF e Nome")
    for cpfPessoa in bancoDeDados:
        print("CPF: {}, Nome: {}".format(bancoDeDados[cpfPessoa], bancoDeDados[cpfPessoa]["nome"]))

def consultaPessoa():
    cpfPessoa = input("Insira o CPF para consulta: ")
    if cpfPessoa in bancoDeDados:
        print("CPF: {}".format(bancoDeDados[cpfPessoa]))
        print("Nome: {}".format(bancoDeDados[cpfPessoa]["nome"]))
        print("Idade: {}".format(bancoDeDados[cpfPessoa]["idade"]))
    else:
        print("CPF não cadastrado!")

def alteracaoNome():
    cpfPessoa = input("Insira o CPF para alteração do nome: ")
    if cpfPessoa in bancoDeDados:
        novoNome = input("Digite o novo nome: ")
        bancoDeDados[cpfPessoa]["nome"] = novoNome
    else:
        print("CPF não encontrado!")

def alteracaoIdade():
    cpfPessoa = input("Insira o CPF para alteração da idade")
    if cpfPessoa in bancoDeDados:
        novaIdade = int(input("Digite a nova idade: "))
        bancoDeDados[cpfPessoa]["idade"] = novaIdade
    else:
        print("CPF não encontrado!")

def deletarCadastro():
    cpfPessoa = input("Insira o CPF que deseja deletar: ")
    if cpfPessoa in bancoDeDados:
        del bancoDeDados[cpfPessoa]
        print("CPF deletado com sucesso!")
    else:
        print("CPF não encontrado")


# ------------------EXECUÇÃO--------------------------------------
opcao = 0
while opcao <= 6:

    opcao = int(input("Escolha a opção: \n1 - Cadastro"
                      "\n2 - Listar as pessoas cadastradas "
                      "\n3 - Consulta por CPF "
                      "\n4 - Alteração de nome"
                      "\n5 - Alteração de idade"
                      "\n6 - Deletar uma pessoa\n"))

    if opcao == 1:
        cadastroPessoas()
    elif opcao == 2:
        listarPessoas()
    elif opcao == 3:
        consultaPessoa()
    elif opcao == 4:
        alteracaoNome()
    elif opcao == 5:
        alteracaoIdade()
    elif opcao == 6:
        deletarCadastro()