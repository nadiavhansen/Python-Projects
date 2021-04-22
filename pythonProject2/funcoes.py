#definir funcao
# def nome():
#     pass

def cliente(nome: str, cpf: str) -> tuple: #retorna uma tupla, pode ser string, etc, não é necessário
    return nome, cpf

print(cliente("Gustavo","48486081"))

def cliente(**kwargs) -> tuple: #retorna uma tupla, pode ser string, etc, não é necessário
    return kwargs("nome"), kwargs("cpf")

print(cliente(nome=Gustavo, cpf=48486081))