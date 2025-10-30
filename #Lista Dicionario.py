#Lista Dicionario
#Questão 1
aluno = {
    "nome": "Pedro Henrique",
    "Idade": "18",
    "curso": "psicologia"
}
print(aluno["nome"])
print(aluno["Idade"])
print(aluno["curso"])

#Exercicio 2
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}
produto["marca"] = "Red dragon"
produto["preco"] = 320,00
produto["estoque"] = produto["estoque"] = 2
produto.pop("marca")

#Exercicio 3
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
print(notas)
media = (notas["Alice"] + notas["Bruno"] + notas["Carla"] + notas["Daniel"]) / 4
print(media)

#Exercicio 4
valores = {"a": 10, "b": 20, "c": 30}
soma = valores["a"] + valores["b"] + valores["c"]
print(soma)

#Exercicio 5
frutas = ["Banana", "Laranja", "Banana", "Uva", "Uva", "Banana", "Laranja", "Uva", "Maçã"]
cont = {}
for item in frutas:
    if item in cont:
        cont[item] += 1
    else:
        cont[item] = 1
print(cont)

#Exercicio 6
produtos = {"Caneta": 10,
            "Mochila": 80,
            "Caderno": 45,
            "Notebook": 3000
            }
for produto, preco in produtos.items():
    if preco >=50:
        print(produto, "=", preco)

#Exercicio 7
pingles = {
    "Door": "Porta",
    "Hello": "Olá",
    "Backpack": "Mochila",
    "Phone": "Telefone"
}
palavra = str(input("Digite uma palavra: "))
if palavra in pingles:
    print(f"A tradução de {palavra} é {pingles[palavra]}")
else:
    print("Palavra não encontrada")

#Exercicio 8
compras = {}
remover = input("Removem item")
produto = input("Digite o produto")
quantidade = int(input("Digite a quantidade"))
if remover == "não":
    if produto in compras:
        compras[produto] = compras[produto] + quantidade
        else:
        compras[produto] = quantidade

#Exercicio 9
turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
turma["Lucas"] = {"idade": 16, "notas": [7, 8, 9]}
print("Médias dos alunos:")
for aluno, dados in turma.items():
    media = sum(dados["notas"]) / len(dados["notas"])
    print(f"{aluno}: Média {media:.1f}")
maior_media = 0
aluno_maior_media = ""

for aluno, dados in turma.items():
    media = sum(dados["notas"]) / len(dados["notas"])
    if media > maior_media:
        maior_media = media
        aluno_maior_media = aluno

print(f"\nAluno com a maior média: {aluno_maior_media}")

#Exercicio 10
funcionarios = {}

def cadastrar_funcionario():
    nome = input("Nome do funcionário: ")
    cargo = input("Cargo do funcionário: ")
    salario = float(input("Salário do funcionário: "))

    funcionarios[nome] = {
        "cargo": cargo,
        "salario": salario
    }
    print(f"Funcionário '{nome}' cadastrado com sucesso!\n")
def consultar_funcionario():
    nome = input("Digite o nome do funcionário para consultar: ")
    if nome in funcionarios:
        dados = funcionarios[nome]
        print(f"\nNome: {nome}")
        print(f"Cargo: {dados['cargo']}")
        print(f"Salário: R$ {dados['salario']:.2f}\n")
    else:
        print(f"\nFuncionário '{nome}' não encontrado.\n")
while True:
    print("Menu:")
    print("1 - Cadastrar funcionário")
    print("2 - Consultar funcionário")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_funcionario()
    elif opcao == "2":
        consultar_funcionario()
    elif opcao == "3":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")