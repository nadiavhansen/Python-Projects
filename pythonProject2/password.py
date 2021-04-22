# Criando uma variável global para a soma dos scores

totscore = 0
import string


# Criando as funções

def NumberOfCharacters(password):
    global totscore
    score = len(password) * 4
    totscore += score
#    print(score)
    return ["Number Of Characters", score]
#NumberOfCharacters("ab88vv54 c")

def UppercaseLetters(password):
    global totscore
    n = 0
    for letra in range(len(password)):
        if password[letra].isupper() and password[letra] in string.ascii_letters:
            n += 1
    if n > 0:
        score = (len(password) - n) * 2
    else:
        score = 0
    totscore += score
    return ["UppercaseLetters", score]

def LowerLetters(password):
    global totscore
    n = 0
    for letra in range(len(password)):
        if password[letra].islower() and password[letra] in string.ascii_letters:
            n += 1
    if n > 0:
        score = (len(password) - n) * 2
    totscore += score
    return ["Lower Letters", score]

def Numbers(password):
    global totscore
    n = 0
    if password.isdigit():
        pass
    else:
        for num in range(len(password)):
            if password[num].isdigit():
                n += 1
    score = n * 4
    totscore += 1
#    print(score)
    return ["Numbers", score]
#Numbers("0123456789a")

def Symbols(password):


