import pymongo
import pandas as pd
from bson.objectid import ObjectId

class BancoDeDados:

    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.conn["Cadastro"]
        self.informacoes = self.db["informacoes"]

    def cadastro_novos_pets(self):
        nome = input("Digite o nome do pet: ")
        animal = input("Digite o animal: ")
        raca = input("Digite a raça do pet: ")
        idade = int(input("Digite a idade do pet: "))
        documento = input("Digite o registro do pet: ")
        pet = dict(nome=f"{nome}", animal=f"{animal}", raca=f"{raca}", idade=f"{idade}", registro=f"{documento}")
        self.informacoes.insert_one(pet)

    def listar_pets_cadastrados(self):
        for i in self.informacoes.find():
            print(i)

        print(pd.DataFrame(self.informacoes.find()))

    def consulta_pet_por_nome(self):
        nome = "Doroteia"
        print(list(self.informacoes.find({"nome": f"{nome}"})))

    def consulta_pet_por_raca(self):
        raca = "Poodle"
        self.informacoes.find({"raca": f"{raca}"})

    def consulta_por_animal(self):
        animal = "Cachorro"
        for i in self.informacoes.find({"animal":f"{animal}"}):
            print(i)

    def alteracao_cadastro_nome(self):
        nome = "Doroteia"
        novo_nome = "Amelia"
        self.informacoes.update_one({"nome": f"{nome}"}, {"$set": {"nome": f"{novo_nome}"}})

    def alteracao_cadastro_idade(self):
        nome = "Amelia"
        nova_idade = 6
        self.informacoes.update_one({"nome": f"{nome}"}, {"$set": {"idade": f"{nova_idade}"}})

    def deletar_cadastro(self):
        # documento = "123"
        # self.informacoes.delete_one({"registro": f"{documento}"})
        # self.informacoes.delete_many({"nome": "Bono"})
        self.informacoes.delete_one({"_id": ObjectId("607f0581846519c7e06b8497")})

    def menu(self):
        opcao = input("""PetShop
                      \n1 - Cadastro Novo Pet
                      \n2 - Consulta
                      \n3 - Alteração de Cadastro
                      \n4 - Deletar Cadastro
                      \n5 - Sair\nOpção: """)
        if opcao == "1": self.cadastro_novos_pets(), self.menu()
        elif opcao == "2":
            nova_opcao = input("""1 - Consulta por Nome
            \n2 - Consulta por Raça
            \n3 - Consulta por Animal\nOpção: """)
            if nova_opcao == "1": self.consulta_pet_por_nome(), self.menu()
            elif nova_opcao == "2": self.consulta_pet_por_raca(), self.menu()
            elif nova_opcao == "3":self.consulta_por_animal(), self.menu()
            else: self.menu()
        elif opcao == "3":
            nova_opcao = input("""1 - Alterar Nome
            \n2 - Alterar Idade\nOpção: """)
            if nova_opcao == "1": self.alteracao_cadastro_nome()
            elif nova_opcao == "2": self.alteracao_cadastro_idade()
            else: self.menu()
        elif opcao == "4": self.deletar_cadastro(), self.menu()
        elif opcao == "5": pass
        else: print("Opção inválida!"), self.menu()


teste = BancoDeDados()
teste.__init__()
# teste.consulta_pet_por_nome()
# teste.listar_pets_cadastrados()
# teste.alteracao_cadastro_nome()
# teste.alteracao_cadastro_idade()
teste.deletar_cadastro()
# teste.cadastro_novos_pets()
# teste.consulta_por_animal()
# teste.menu()