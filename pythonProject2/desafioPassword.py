# Regras de negócio
# numeros de caracteres = numero de caracteres * 4
# Uppercase Letters = (len total - len uppercase) * 2
# Lowercase Letters = (len total - len lowercase) * 2
# Numbers = quantidade de numeros * 4
# Symbols = quantidade de simbolos * 6
# Middle Numbers or Symbols = quantidade de simbolos entre letras e numeros * 2
# Requirements = quantidade de requerimentos atendidos (upper, lower, numbers, symbols) * 2

# letters only = quantidade de letras * -1
# numbers only = quantidade de numeros * -1
# Consecutive Uppercase Letters = letras maiusculas iguais seguidas * -2
# Consecutive Lowercase Letters = letras maiusculas iguais seguidas * -2
# Consecutive Numbers = numeros iguais seguidos * -2
# Sequential Letters (3+) = letras consecutivas (abc...) * -3
# Sequential Numbers (3+) = numeros consecutivas (123...) * -3
# Sequential Symbols (3+) = símbolos consecutivas (!@#...) * -3

#password = input("Senha: ")

import string
totscore = 0

def NumberOfCharacters(password):
    global totscore
    score = 4 * len(password)
    totscore += score
#    print(score)
    return ["Numbers of Characters", score]
#NumberOfCharacters("12345")

def UpperLetters(password):
    global totscore
    n = 0
    for letra in range(len(password)):
        if password[letra].isupper() and password[letra] in string.ascii_letters:
            n += 1
    if n > 0:
        score = (len(password)-n) * 2
    else:
        score = 0
    totscore += score
#    print(score)
    return ["Upper Letters", score]
#UpperLetters("ABCabDe5!raSaaaaaa")

def LowerLetters(password):
    global totscore
    n = 0
    for letra in range(len(password)):
        if password[letra].islower() and password[letra] in string.ascii_letters:
            n += 1
    if n > 0:
        score = (len(password)-n) * 2
    else:
        score = 0
    totscore += score
#    print(score)
    return ["Lower Letters", score]
#LowerLetters("ABCabDe5!raSaaaaaa")

def Numbers(password):
    global totscore
    n = 0
    if not password.isdigit():
        for num in range(len(password)):
            if password[num].isnumeric():
                n += 1
    score = n * 4
    totscore += score
#    print(score)
    return ["Numbers", score]
#Numbers("12frf84t8#eRt5.")

def Symbols(password):
    global totscore
    n = 0
    for symbol in range(len(password)):
        if not password[symbol] in string.ascii_letters and not password[symbol].isdigit()\
                and not password[symbol] in " _": #isdigit é isnumero
            n += 1
    score = n * 6
    totscore += score
#    print(score)
#    print(n)
    return ["Symbols", score]
#Symbols("!@#ád")

def MiddleNumbersSymbols(password):
    global totscore
    n = 0
    password = password[1:-1]
#    print(password)
    lista = password.split()
    password = "".join(lista)
    for char in range(len(password)):
        if not password[char] in string.ascii_letters and password[char] not in " _":
            n += 1
    score = n * 2
    totscore += score
#    print(score)
    return ["Middle Numbers Symbols", score]
#MiddleNumbersSymbols("!@#821")

def Requirements(password):
    global totscore
    score = 0

    if len(password) >= 8:
        score += 1


        #Entra se houver maiuscula
        if not password.lower() == password:
            score += 1
            #print(1)
        #entra se houver minuscula
        if not password.upper() == password:
            score += 1
            #print(2)
        #entra se houver simbolo
        if not password.isdigit() and password in string.ascii_letters and password not in " _":
            score += 1
            #print(3)
        #entra se houver numero
        if any(True for letra in password if letra.isdigit()):
            score += 1
            #print(4)

    if score < 4: score= 0
    score = score * 2
    totscore += score
#    print(score)
    return ["Requirements", score]
#Requirements("abácadabr4")

def LettersOnly(password):
    n = 0
    score = 0
    global totscore
    if password.isalpha():
        for letra in range(len(password)):
            if password[letra].isalpha():
                n += 1
        score = (n * (-1))
    totscore += score
#    print(score)
    return ["Letters Only", score]
#LettersOnly("hhhhhryryHHYT")

def NumbersOnly(password):
    global totscore
    score = 0
    n = 0
    if password.isdigit():
        for num in range(len(password)):
            if password[num].isdigit() and password[num]:
                n += 1
                score = n * (-1)
    totscore += score
#    print(score)
    return ["NumbersOnly", score]
#NumbersOnly("128286548888")

def ConsecutiveUppercaseLetters(password):
    global totscore
    n = 0
    # if len(password) % 2 != 0:
    # para adicionar um caractere que não é letra maiuscula no final, para considerar senha par ou ímpar
    password = password + "!"

    for letra in range(len(password)):
        if password[letra].isupper() and password[letra + 1].isupper() \
                and password[letra] in string.ascii_letters and password[letra + 1] in string.ascii_letters:
            n += 1
    score = n * (-2)
    totscore += score
#    print(score)
    return ["Consecutive Uppercase Letters", score]
#ConsecutiveUppercaseLetters("fffJJdusAUIdEDD")

def ConsecutiveLowercaseLetters(password):
    global totscore
    n = 0
    # para adicionar um caractere que não é letra minuscula no final, para considerar senha par ou ímpar
    password = password + "!"

    for letra in range(len(password)):
            if password[letra].islower() and password[letra + 1].islower() \
                    and password[letra] in string.ascii_letters and password[letra + 1] in string.ascii_letters\
                    and password[letra] not in " ":
                n += 1
    score = n * (-2)
    totscore += score
#    print(score)
    return ["Consecutive Lowercase Letters", score]
#ConsecutiveLowercaseLetters("fffJJdusAUIdEDD")

def ConsecutiveNumbers(password):
    global totscore
    n = 0
    password = password + "!"
    for num in range(len(password)):
        if password[num].isnumeric() and password[num + 1].isnumeric():
            n += 1
    score = n * (-2)
    totscore += score
#    print(score)
    return ["Consecutive Numbers", score]

#ConsecutiveNumbers("123456789fdsf818gg5g818g28g")

def SequentialLetters(password):
    global totscore
    n = 0
    password = password + "!!"
    setpassword = set()
    for letra in range(len(password) - 2):
        sequencia = password[letra].lower() + password[letra + 1].lower() + password[letra + 2].lower()
        if sequencia in string.ascii_lowercase:
            setpassword.add(sequencia)
    n = len(setpassword)
    score = (n * (-3))
    totscore += score
#    print(score)
    return ["Sequential Letters", score]
#SequentialLetters("abcfdefrghiabcabc")

def SequentialNumbers(password):
    global totscore
    n = 0
    password = password + "!!"
    setpassword = set()
    for num in range(len(password) - 2):
        sequencia = password[num] + password[num + 1] + password[num + 2]
        if sequencia in "0123456789":
            setpassword.add(sequencia)
    n = len(setpassword)
    score = n * (-3)
    totscore += score
#    print(score)
    return ["SequentialNumbers", score]

#SequentialNumbers("012dddd456fff012hn567uyg")

# def SequentialSymbols(password):
#     n = 0
#     password = password + "aa"
#     for symbol in range(len(password) - 2):
#         if password[symbol] + password[symbol + 1] + password[symbol + 2] in "!@#$%" and "&*(":
#             n += 1
#             score = n * (-3)
#     print(score)
#     return ["Sequential Symbols", score]
#
# SequentialSymbols("!@#aaaa@#$aaaa%&*aaa)_+aaa!@#aaaaaa%&*")

# ------------------------------------------------------------------------------
# EXECUÇÃO
password = input("Senha: ")

# Coloquei todas as funções em uma lista para chamá-las no for abaixo:
listafuncoes = [NumberOfCharacters, UpperLetters, LowerLetters, Numbers, Symbols, MiddleNumbersSymbols,
                Requirements, LettersOnly, NumbersOnly, ConsecutiveUppercaseLetters, ConsecutiveLowercaseLetters,
                ConsecutiveNumbers, SequentialLetters, SequentialNumbers]

for func in listafuncoes:
    resultado = func(password)
    print(resultado)

    if totscore < 0:
        totscore = 0
    if totscore > 100:
        totscore = 100

print(totscore)




def executar(password):
    global totscore
    totscore = 0
    for func in listafuncoes:
        resultado = func(password)
 #       print(resultado)

    if totscore < 0:
        totscore = 0
    if totscore > 100:
        totscore = 100

    return totscore


testes = []

testes.append(("Teste1", 36))
testes.append(("Aa$%9w012", 100))
testes.append(("AWEpoiu", 25))
testes.append(("1234567890", 7))
testes.append(("imaginesó", 30))
testes.append(("á$%012ó~w", 100))
testes.append(("awd01002", 58))
testes.append(("8909801123á", 87))
testes.append(("abcabc123123", 68))
testes.append(("abácadabr4", 52))
testes.append(("_teste sobre isso__", 41))
testes.append(("!d$%*5 w", 88))
testes.append(("MEUNOME", 9))
testes.append(("meunome", 9))
testes.append(("AbCnomeABcMNo", 49))
testes.append(("<>@!_ *(#", 88))
testes.append(("_awDad_ ", 42))


for i in testes:
    nota = executar(i[0])
    if nota == i[1]:
        print(f"O teste {i[0]} foi correto!")
    else:
        print(f"O teste {i[0]} foi diferente! Esperado: {i[1]}, recebido: {nota}")



