# 1 – Crie uma calculadora que faça as operações básicas (+ - / *)

operacao = ""
resultado = 0

while True:

    num1 = float(input("Digite um número: "))
    operacao = input("Digite a operação desejada (sendo '+', '-', '*' ou '/', e 0 para parar): ")
    if operacao == "0":
        break
    else:
        num2 = float(input("Digite um número: "))
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2

    print("Resultado= {}".format(resultado))

