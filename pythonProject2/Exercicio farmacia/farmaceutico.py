import datetime


class Paciente:

    def __init__(self, nome_medicamento, validade_medicamento, quantidade, nome_paciente_receita,
                 cpf, nome_paciente_documento):
        self.receita = [nome_medicamento, validade_medicamento, quantidade, nome_paciente_receita]
        self.documento = [cpf, nome_paciente_documento]


class Farmaceutico():

    def receber_receita_e_documento(self, paciente: Paciente):
        self.receita_recebida = paciente.receita
        self.documento_recebido = paciente.documento

    def validar_receita(self):
        validacoes = bool
        data_formatada_receita = (datetime.datetime.strptime(self.receita_recebida[1], "%d/%m/%Y"))

        if self.receita_recebida[3] == self.documento_recebido[1] and \
                data_formatada_receita >= datetime.datetime.today():
            validacoes = True
            return validacoes
        # else:
        #     if self.receita_recebida[3] != self.documento_recebido[1]:
        #         print("O nome da receita não coincide com o nome do documento!")
        #     if data_formatada_receita < datetime.datetime.today():
        #         print("A receita está vencida!")

        return False

    def verificar_estoque(self):

        if not self.validar_receita():
            print("Receita inválida!")

        if self.validar_receita():
            with open("Estoque.txt", "r") as file:
                estoque = file.readlines()
                situacao = bool

                for linha in range(len(estoque)):
                    (estoque[linha]).strip().split(',')
                    if self.receita_recebida[0] == ((estoque[linha]).split(','))[0] and \
                            self.receita_recebida[2] <= int(((estoque[linha]).split(','))[1]):
                        situacao = True
                        break
                    else:
                        situacao = False
            return situacao


    def retirar_do_estoque(self):

        if self.verificar_estoque():

            with open("Estoque.txt", "r") as file:
                estoque = file.readlines()

                for linha in range(len(estoque)):
                    if self.receita_recebida[0] == ((estoque[linha]).split(','))[0]:
                        nova_quantidade = int(((estoque[linha]).split(','))[1]) - self.receita_recebida[2]
                        estoque[linha] = f"{estoque[linha].strip().split(',')[0]},{nova_quantidade}\n"

            with open("Estoque.txt", "w") as file:
                file.write("".join(estoque))

        else:
            pass

    def entregar_medicamento(self):
        if self.validar_receita() and self.verificar_estoque():
            print(f"\nMedicamento: {self.receita_recebida[0]}\nQuantidade: {self.receita_recebida[2]}\nAté mais!!")
        elif not self.validar_receita():
            print('A receita não é valida!')
        elif not self.verificar_estoque():
            print('Não temos no estoque! Sinto muito :(')


def executar():
    print("---Bem vindo a farmácia do SUS---\n\n---Receita---")
    nome_medicamento = input("Digite o nome do medicamento: ")
    validade_receita = input("Digite a data de validade da receita (dd/mm/yyyy): ")
    quantidade = int(input("Digite a quantidade: "))
    nome_paciente_receita = input("Digite o nome do paciente na receita: ")
    print("---Documento paciente---")
    cpf = input("Digite o CPF do paciente: ")
    nome_paciente_documento = input("Digite o nome do paciente no documento: ")

    a = Paciente(nome_medicamento, validade_receita, quantidade, nome_paciente_receita, cpf, nome_paciente_documento)

    paciente = Farmaceutico()
    paciente.receber_receita_e_documento(a)
    paciente.entregar_medicamento()


executar()


# a = Farmaceutico()
# 
# print(a.receber_receita('Neosaldina','18/04',2,'paulo'))
# a.validar_receita()
# print(a.verificar_estoque())

# with open("Receita.txt", "r") as file:
#     receita = file.readlines()
#     receita = "".join(receita)
# return receita

# b = Paciente()

# with open("Paciente.txt", "r") as file_paciente:
#     paciente = file_paciente.readlines()

# self.receita = {'nome_medicamento': nome_medicamento,
#                 'validade_medicamento': validade_medicamento,
#                 'quantidade': quantidade,
#                 'nome_paciente': nome_paciente}
# self.documento = {'cpf': cpf, 'nome_paciente': nome_paciente}

#and\self.receita_recebida[2] >= int(((estoque[linha]).split(','))[1]):


# a = Paciente('Torsilax', '18/04/2021', 2, 'Ana', "000", 'Ana')
# print(a.receita)
#
# b = Farmaceutico()
# b.receber_receita_e_documento(a)
# print(b.receita_recebida)
# print(b.documento_recebido)
# print('')
# print('---validar receita---')
# print(b.validar_receita())
# print('---verificar estoque---')
# print(b.verificar_estoque())
# print('---retirar estoque---')
# print(b.retirar_do_estoque())
# print('---entregar medicamento---')
# b.entregar_medicamento()