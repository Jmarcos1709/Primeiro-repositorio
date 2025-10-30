#Exercício1
idade1 = 18
altura = 1.81
nome = "João Marcos"
eh_estudante = True
print(type(idade1))
print(type(altura))
print(type(nome))
print(type(eh_estudante))

#Exercício 2
idade = input("Digite sua idade")
idade = int (idade) + 5
print (f"Sua idade em 5 anos será: {idade}")

#Exercício 3
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print (f"a soma é: {soma}")

#Exercício 4
num3 = int(input("Digite o primeiro número: "))
num4 = int(input("Digite o segundo número: "))
num5 = int(input("Digite o terceiro número: "))
media = (num3 + num4 + num5)/3
print(f"Sua média é: {media}")

#Exercício 5
nota1 = float(input("Digite a nota da AC: "))
nota2 = float(input("Digite a nota da AP1: "))
nota3 = float(input("Digite a nota da AP2: "))
notafinal = (0.2 * nota1) + (0.4 * nota2) + (0.4 * nota3)
print(f"Sua nota final é: {notafinal}") 
print(f"Sua nota final é: {notafinal}")
if notafinal >= 7:
    print(str("Aprovado"))
else:
    print(str("Reprovado"))

#Exercício 6 
nomecompleto = str(input("Digite seu nome aqui: "))
print(nomecompleto.split()[0])
print(len(nomecompleto))
print(nomecompleto.upper())
