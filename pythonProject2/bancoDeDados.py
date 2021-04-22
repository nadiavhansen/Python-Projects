import MySQLdb

conn = MySQLdb.connect(db="Llama", host="localhost", port=3306, user="root")
cursor = conn.cursor()
#
#
# cursor.execute("select * from aqui")
# # print(cursor.fetchall())
# for i in cursor.fetchall():
#     print(i)
# print('-'*100)
#
#
# cursor.fetchall()
# print(cursor.description) #para pegar o nome da coluna (ignorar os números, é coisa padrao do bd)
# print('-'*100)
#
#
# for col in cursor.description:
#     print(col[0]) #para pegar o nome de cada coluna
# print('-'*100)
#
#
# nome = input("Digite o nome: ")
# cpf = input("Digite o cpf: ")
#
# cursor.execute(f"INSERT INTO aqui VALUES ('{nome}', DEFAULT, '{cpf}')")
# conn.commit() #para enviar para o banco de dados
#
# cursor.execute("INSERT INTO aqui (Nome, Cpf) VALUES ('481', '871')")
#
#
# nome = input("Digite o nome: ")
# # alterando o nome de quem tem o cpf 002
# sql = f"""
#     UPDATE aqui
#     SET Nome = '{nome}'
#     WHERE cpf = '123'
#     """
# cursor.execute(sql)
# conn.commit()

# sql = f"""
#     DELETE FROM aqui
#     WHERE cpf = '123'
#     """
# cursor.execute(sql)
# conn.commit()




# sql = f"Update aqui "\
#     f"Set Nome = '{nome}'"\
#     f"where cpf = '0010'"