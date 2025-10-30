#Loop1
#Exercicio 1
frutas = ["maçã", "banana", "laranja", "uva"]

#Exercicio 2
print(frutas[0])
print(frutas[-1])

#Exercicio 3
frutas.append("manga")

print(frutas)

#Exercicio 4
frutas.remove("banana")

print(frutas)

#Exercicio 5
indice = frutas.index("laranja")
frutas[indice] = "abacaxi"

#Exercicio 6
list_num = list(range(1,11))
print(list_num)

#Exercicio 7
soma = sum(list_num)
print(soma)

#Exercicio 8
max(list_num)
min(list_num)

#Exercicio 9
list(reversed(list_num))

#Exercicio 10
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]

#Exercicio 11
sorted(cidades)

#Exercicio 12
cidades.append("Porto Alegre")
cidades.insert(-1, "Porto Alegre")

#Exercicio 13
cidades.index("Curitiba")

#Exercicio 14
cidades.remove("Rio de Janeiro")

#Exercicio 15
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

#Exercicio 16
lista3 = lista1 + lista2

#Exercicio 21
nomes = ['Ana', 'Pedro', 'Maria', 'João']

#Exercicio 22
for nome in nomes:
    print(nome)

#Exercicio 23
nomes_maiusculos = []

#Exercicio 24
for par in numeros:
    if par % 2 == 0:
        print(par)

#Exercicio 25
for value in numeros:
    quadrados.append(value**2)

print(quadrados)

#Exercicio 26
palavras = ["python", "java", "c", "javascript"]
for value in palavras:
    print(len(value))

#Exercicio 27
idades = [12, 18, 25, 40, 60]
for idade in idades:
    if idade <= 18:
        print("Menor de idade")
    else:
        print("Maior de idade")

#Exercicio 28
notas = [5.5, 7.0, 8.3, 4.9, 6.2]

aprovados = 0
reprovados = 0

for nota in notas: 
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1
print(aprovados)
print(reprovados)

#Exercicio 29
palíndromos = []
não_palindromos = []

palavras_2 = ["arara", "banana", "radar", "python"]
for palavra in palavras_2:
    if palavra == palavra[::-1]:
        palíndromos.append(palavra)
    else:
        não_palindromos.append(palavra)

print(palíndromos)

#Exercicio 30
compras = ["arroz", "feijão", "batata", "carne"]
for value in compras:
    print(f"Preciso comprar: {value}")

# -----------------------------------------------------------------

#Exercicio 31
numero_2 = 1

while numero_2 <= 10:
    print(numero_2)
    numero_2 += 1

#Exercicio 32
numero_int = int(input("Digite um número"))

while numero_int != 0:
    print(f"Você digitou: {numero_int}")
    numero_int = int(input("Digite outro número"))

print("programa encerrado")

#Exercicio 33
numeros_range = 1
soma = 0

while numeros_range < 100: 
    soma += numeros_range
    numeros_range += 1

print(soma)

#Exercicio 34.
secreto = int(input("DIgite até acertar o número secreto: "))

while secreto != 7:
    print("Numero errado")
    secreto = int(input("DIgite até acertar o número secreto: "))

print("Numero correto")

# Exercício 35
pares = 2

while pares <= 20 and pares % 2 == 0:
    print(pares)
    pares += 2
