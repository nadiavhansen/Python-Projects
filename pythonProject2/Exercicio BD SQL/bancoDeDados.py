import MySQLdb


class BancoDeDados:

    def __init__(self):
        self.conn = MySQLdb.connect(db="cadastro", host="localhost", port=3306, user="root")
        self.cursor = self.conn.cursor()

    def exibir_informacoes(self):
        self.cursor.execute("select * from informacoes")
        print("Nome\t  CPF\t\tIdade\tAltura")
        for i in self.cursor.fetchall():
            # print(f"""{i[1]} - {i[2]} - {i[3]} - {i[4]}""")
            # print("  -  ".join([str(item) for item in i if item != i[0]]))
            print("  -  ".join([str(item) for item in i[1:]]))


    def criar_novo_cadastro(self):
        print("---------- Cadastro ----------")
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        idade = int(input("Digite a idade: "))
        altura = int(input("Digite a altura (em cm): "))
        verificacao = self.cursor.execute(f"""SELECT CPF FROM informacoes WHERE CPF = '{cpf}'""")

        if verificacao == 1:
            print("CPF já cadastrado!")
            self.criar_novo_cadastro()
        else:
            self.cursor.execute(f"""INSERT INTO informacoes VALUES
                                (DEFAULT, '{nome}', '{cpf}', '{idade}', '{altura}')""")
            self.conn.commit()
            print("\nCadastro realizado com sucesso!")

    def pesquisar_cadastro_por_cpf(self):
        print("---------- Cadastro ----------")
        cpf = input("Digite o CPF para pesquisa: ")
        self.cursor.execute(f"""SELECT * FROM informacoes WHERE CPF = '{cpf}'""")
        for i in self.cursor.fetchall():
            print(f"\nNome: {i[1]}\nCPF: {i[2]}\nIdade: {i[3]}\nAltura: {i[4]}")

    def alterar_cadastro(self):
       print("---------- Alterar Cadastro ----------")
       cpf = input("Digite o CPF para alteração: ")
       verificacao = self.cursor.execute(f"""SELECT CPF FROM informacoes WHERE CPF = '{cpf}'""")
       if verificacao != 1:
            print("\nCPF inválido! Tente novamente.")
            self.alterar_cadastro()

       info = input("Digite o que você deseja alterar: "
                        "\n1 - Nome"
                        "\n2 - Idade"
                        "\n3 - Altura\nOpção: ")
       if info == '1':
           novo_nome = input("Digite o novo nome: ")
           self.cursor.execute(f"""UPDATE informacoes SET Nome = '{novo_nome}' WHERE CPF = '{cpf}'""")
       elif info == '2':
           nova_idade = int(input("Digite a nova idade: "))
           self.cursor.execute(f"""UPDATE informacoes SET Idade = '{nova_idade}' WHERE CPF = '{cpf}'""")
       elif info == '3':
           nova_altura = int(input("Digite a nova altura: "))
           self.cursor.execute(f"""UPDATE informacoes SET Altura = '{nova_altura}' WHERE CPF = '{cpf}'""")
       else:
           print("\nOpção inválida. Tente novamente!"), self.alterar_cadastro()
       self.conn.commit()

    def deletar_cadastro(self):
        print("---------- Deletar Cadastro ----------")
        cpf = input("Digite o CPF para deletar o cadastro: ")
        verificacao = self.cursor.execute(f"""SELECT CPF FROM informacoes WHERE CPF = '{cpf}'""")
        if verificacao != 1:
            print("CPF inválido! Tente novamente.")
            self.deletar_cadastro()
        else:
            self.cursor.execute(f"""DELETE FROM informacoes WHERE CPF = '{cpf}'""")
            self.conn.commit()
            print("\nCadastro deletado com sucesso!")

    def menu_cadastro(self):
        print("-="*10 + "Sistema de cadastros" + "-="*10)
        opcao = input("1 - Novo Cadastro"
                        "\n2 - Alterar Cadastro"
                        "\n3 - Consultar cadastro por CPF"
                        "\n4 - Exibir cadastros existentes"
                        "\n5 - Deletar Cadastro"
                        "\n6 - Sair"
                        "\nOpção: ")
        if opcao == "1": self.criar_novo_cadastro(), self.menu_cadastro()
        elif opcao == "2": self.alterar_cadastro(), self.menu_cadastro()
        elif opcao == "3": self.pesquisar_cadastro_por_cpf(), self.menu_cadastro()
        elif opcao == "4": self.exibir_informacoes(), self.menu_cadastro()
        elif opcao == "5": self.deletar_cadastro(), self.menu_cadastro()
        elif opcao == "6": print("-="*12 + "Até mais!!" + "-="*13)
        else: print("Opção inválida! Tente novamente."), self.menu_cadastro()

def executar():
    a = BancoDeDados()
    a.menu_cadastro()

executar()


#
# a = BancoDeDados()
# a.exibir_informacoes()
# # a.criar_novo_cadastro()
# a.pesquisar_cadastro_por_cpf()
# # a.alterar_cadastro()
# # a.deletar_cadastro()