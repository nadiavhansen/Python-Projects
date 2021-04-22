# AVALIAÇÃO DE FORÇA DO PASSWORD
# http://www.passwordmeter.com/
import string

# FUNÇÕES QUE SERÃO CHAMADAS PELA FUNÇÃO PRINCIPAL
# Calcula o total de caracteres
def NumberChar(password):
    pontos = 4 * len(password)
    return ["Number of Characters", pontos]

# Computa os caracteres em uppercase
def Uppercase_letters(password):
    n = sum(1 for letra in password if letra in string.ascii_uppercase)
    if n > 0:
        pontos = (len(password) - n) * 2
    elif n == len(password):  # tudo é uppercase
        pontos = 0
    else:
        pontos = 0
    return ["Uppercase letters", pontos]

# Computa os caracteres em lowercase
# Se tudo for lowercase, não pontua.
def Lowercase_letters(password):
    n = sum(1 for letra in password if letra in string.ascii_lowercase)
    if n > 0:
        pontos = (len(password) - n) * 2
    elif n == len(password):  # tudo é lowercase
        pontos = 0
    else:
        pontos = 0
    return ["Lowercase letters", pontos]

# Computa os caracteres que são números
# Se tudo for númérico, não pontua.
def Numbers(password):
    n = sum(1 for letra in password if letra.isnumeric())
    pontos = n * 4
    if n == len(password):  # tudo é number
        pontos = 0
    return ["Numbers", pontos]


def Symbols(password):
    n = sum(1 for letra in password if not letra in string.ascii_letters
            and not letra.isnumeric() and not letra in [" ", "_"])
    pontos = n * 6
    return ["Symbols", pontos]


def MiddleNumbersSymbols(password):
    newpassword = password[1:-1]
    n = sum(1 for letra in newpassword if letra not in string.ascii_letters
            and letra not in [" ", "_"])
    pontos = n * 2
    return ["Middle Numbers or Symbols", pontos]


def Requirements(password):
    n = 0
    if len(password) > 7:
        n += 1
        if any(True for letra in password if letra in string.ascii_uppercase):
            n += 1
        if any(True for letra in password if letra in string.ascii_lowercase):
            n += 1
        if any(True for letra in password if letra.isnumeric()):
            n += 1
        if any(True for letra in password if letra not in string.ascii_letters
                                             and letra not in [" ", "_"] and not letra.isnumeric()):
            n += 1
    if n < 4: #não atinge o mínimo do que é esperado, logo não computa.
        pontos = 0
    else:
        pontos = n * 2
    return ["Requirements", pontos]


def LettersOnly(password):
    n = sum(1 for letra in password if letra in string.ascii_letters
            or letra in [" ", "_"])
    if len(password) == n:
        pontos = -n
    else:
        pontos = 0
    return ["Letters only", pontos]


def NumbersOnly(password):
    if password.isdigit():
        n = len(password)
        pontos = -n
    else:
        pontos = 0
    return ["Numbers only", pontos]


def ConsecutiveUppercase(password):
    n = 0
    for i in range(len(password) - 1):
        if password[i] in string.ascii_uppercase \
                and password[i + 1] in string.ascii_uppercase:
            n += 1
    pontos = -(n * 2)
    return ["Consecutive Uppercase Letters", pontos]


def ConsecutiveLowercase(password):
    n = 0
    for i in range(len(password) - 1):
        if password[i] in string.ascii_lowercase and password[i + 1] \
                in string.ascii_lowercase + " ":
            n += 1
        pontos = -(n * 2)
    return ["Consecutive Lowercase Letters", pontos]


def ConsecutiveNumbers(password):
    n = 0
    for i in range(len(password) - 1):
        if password[i].isnumeric() and password[i + 1].isnumeric():
            n += 1
        pontos = -(n * 2)
    return ["Consecutive Numbers", pontos]


def SequentialLetters3more(password):
    n = 0
    password = password + "!!"
    setpassword = set()
    for letra in range(len(password) - 2):
        sequencia = password[letra].lower() + password[letra + 1].lower() + \
                    password[letra + 2].lower()
        if sequencia in string.ascii_lowercase:
            setpassword.add(sequencia)
    n = len(setpassword)
    pontos = (n * (-3))
    return ["Sequential Letters (3+)", pontos]

def SequentialNumbers3more(password):
    n = 0
    password = password + "!!"
    setpassword = set()
    for letra in range(len(password) - 2):
        sequencia = password[letra] + password[letra + 1] + password[letra + 2]
        if sequencia in "0123456789":
            setpassword.add(sequencia)
    n = len(setpassword)
    pontos = (n * (-3))
    return ["Sequential Numbers (3+)", pontos]

# ------------------------------------------------------------------------------
# EXECUÇÃO

def executa_password_forte(password):
    listafuncoes = [NumberChar, Uppercase_letters, Lowercase_letters, Numbers, Symbols, MiddleNumbersSymbols,
                    Requirements, LettersOnly, NumbersOnly, ConsecutiveUppercase, ConsecutiveLowercase,
                    ConsecutiveNumbers,
                    SequentialLetters3more, SequentialNumbers3more]
    password = "dsfdvfr"
    Nota = 0
    for func in listafuncoes:
        resultado = func(password)
        print(resultado) #APENAS UTILIZAR QUANDO NAO FOR TESTE
        Nota += (resultado[1])
    if Nota < 0:
        Nota = 0
    if Nota > 100:
        Nota = 100
    print("Score final = " + str(Nota)) #APENAS UTILIZAR QUANDO NAO FOR TESTE
    return Nota

#executa_password_forte("_teste sobre isso__") #APENAS UTILIZAR QUANDO NAO FOR TESTE
#-----------------------------------------------------------------------------------

