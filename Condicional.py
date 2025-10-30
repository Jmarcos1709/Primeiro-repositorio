#Lista 2
#Calculo impar
numdig = int(input("Digite um número inteiro: "))
if numdig % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")

#Calculo aprovação
nota1 = float(input("Digite a nota da AC: "))
nota2 = float(input("Digite a nota da AP1: "))
nota3 = float(input("Digite a nota da AP2: "))
notafinal = (0.2 * nota1) + (0.4 * nota2) + (0.4 * nota3)
print(f"Sua nota final é: {notafinal}")
if notafinal >= 7:
    print(str("Aprovado"))
else:
    print(str("Reprovado"))

#Calculo de desconto
vcompra = float(input("Digite o valor da sua compra: "))
compradesc = vcompra * 0.9
if vcompra > 100:
    print(str("Parabéns, você ganhou 10% de desconto"))
    print(compradesc)
else:
    print(vcompra)

#Exercicio 4
celsius = float(input("Digite a temperatura em celsius: "))
faren = (float(celsius * 9/5) + 32)
print (f"A temperatura em farenheit é: {faren}")

#Exercicio 5
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print("O primeiro número é maior")
if num2 > num1:
    print("O segundo é maior")
if num1 == num2:
    print("Os numeros são iguais")

#Exercicio 6
num3 = float(input("Digite o primeiro número: "))
num4 = float(input("Digite o segundo número: "))
num5 = float(input("Digite o  terceiro número: "))
maior = num3
if maior < num4:
    maior = num4
if maior < num5:
    maior = num5
print(f"O maior número é {maior}")

#Exercicio 7
n1 = float(input("Digite o primeiro número"))
n2 = float(input("Digite o segundo número: "))
op = str(input("Dgite o sinal da operação: "))
if op == "/":
    print(n1 / n2)
if op == "*":
    print(n1 * n2)
if op == "+":
    print(n1 + n2)
if op == "-":
    print(n1 - n2)

#Exercicio 8

#Exercico 9 
ano = int(input("Digite o ano:"))
if ano % 4 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")

#Exercicio 10
idade = float(input("Digite sua idade: "))
if idade >= 18 and idade <= 65:
    print("Você está dentro da faixa permitida")
else:
    print("Você não está na faixa permitida")

#Exercicio 11
user = input("Digite o usuario: ")
senha = input("Digite a senha")
if user == "admin" and senha == "1234":
    print("Acesso liberado")
else:
    print("acesso negado")

#Exercico 12
idade2 = int(input("Digite sua idade: "))

if idade2 >= 18 and idade2 <= 70:
    print("Voto obrigatório")
elif idade2 >= 16 and idade2 <= 18:
    print("Não precisa votar")
else:
    print("Não vota")

#exrcicio 13
inter = int(input("Digite o número: "))

if inter >= 10 and inter <= 50:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")

#Exercicio 14
media = float(input("Digite sua média final: "))
if media >= 7:
    print("Aprovado")
elif media >= 5 and media <= 7:
    print("Recuperação")
else:
    print("Reprovado")