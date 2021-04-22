# password = "ABCDEFGHI"
# print(password)
# password = password + "0"
#
# print(password)
#
# password = password[:-1]
#
# print(password)
#
# import string
# print(string.ascii_letters)

# p = "_testesobreisso__"
# lista = p.split()
# print(p)
# print(lista)
# palavra = "".join(lista)
# print(palavra)

# def Requirements(password):
#     n = 0
#
#     if len(password) > 7:
#         n += 1
#         for char in range(len(password)):
#             if password[char].isupper():
#                 n += 1
#             if password[char].islower():
#                 n += 1
#
#             # if (True for letra in password if letra.isupper()):
#             #     n += 1
#             # if (True for letra in password if letra.islower()):
#             #     n += 1
#             # if (True for letra in password if letra.isdigit()):
#             #     n += 1
#             # if (False for letra in string.ascii_letters if not letra.isdigit()):
#             #     n += 1
#     if n < 4: n = 0
#     score = n * 2
#     print(n)
#     print(score)
#     return ["Requirements", score]
#
# Requirements("2222222222")

a = "aaaaa"
print(a.capitalize())