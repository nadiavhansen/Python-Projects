import pymongo
import bson

conn = pymongo.MongoClient("mongodb://localhost:27017/")

# print(conn.list_database_names())

db = conn["Llama"]
usuarios = db["usuarios"]

pessoa = dict(nome="Teste1", idade=55)
pessoa2 = dict(nome="Teste2", idade=45)
pessoa3 = dict(nome="Teste3", dados=dict(cpf="0000", idade=15, altura=1.7))

usuarios.insert_one(pessoa)

usuarios.insert_many([pessoa, pessoa2])

usuarios.insert_one(pessoa3)

for i in usuarios.find():
    print(i)

for i in usuarios.find({}, {"nome": 1}):
    print(i)

for i in usuarios.find({"_id":0}, {"nome": 1}):
    print(i)