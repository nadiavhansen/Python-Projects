x = "Teste curso de python"

print(x[0])
print(x[-1])
print(x[0:2]) # do zero até o 1 (2 - 1)
print(x[-5:-1])
print(x[0:]) # 0 até o final
print(x[:3]) # do começo até o 2
print(x[::2]) # pula de 2 em 2
print(x[::-1]) # ao contrário
print("")

print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.strip()) #tira espaço
print(x.strip("-")) # tira os ' - '
print(x.split(" ")) # quebra numa lista
print(x.replace("Teste", "Inicio do", 1)) # o numero altera só o primeiro, se não especificar vai trocar todos
print(x.count("teste"))
print(x.lower().count("teste"))
print("")

print(x.isalpha()) # é apenas letras?
print(x.isalnum()) #só letras e numeros?
print(x.isnumeric()) # é apenas números?
print("")

z = "Teste {} um".format("numero")
print(z)

f = "AAA"
g = f"Teste {f}"
print(g)

print("")


y = "Teste numero um"
print(x in y)

a = "Nadia" + " Hansen"
print(a)

b = "Teste " * 3 + "!!"
print(b)

c = str(1209)
print(type(c))

d = """Teste
numero um"""
print(d)

# ctrl + d para clonar
# shift + ALT ^v para subir ou descer
# ctrl + / para comentar varias linhas