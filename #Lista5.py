#Lista5
#Exercicio 1
faturamento = [
 {"dia": "segunda", "valor": 1200},
 {"dia": "terça", "valor": 1500},
 {"dia": "quarta", "valor": 900},
 {"dia": "quinta", "valor": 1800},
 {"dia": "sexta", "valor": 2400},
]
soma = sum(item["valor"] for item in faturamento)
print(soma)

#Exercicio 2
estoque = {
 "notebook": [5, 7, 3],  
 "mouse": [20, 25, 18],
 "teclado": [12, 14, 9],
}
soma2 = sum(sum(qty) for qty in estoque.values())
print(soma2)

#Exercicio 3
funcionarios = [
 {"nome": "Ana", "salario": 4500, "departamento": "RH"},
 {"nome": "Carlos", "salario": 7000, "departamento": "TI"},
 {"nome": "Beatriz", "salario": 5200, "departamento": "Financeiro"},
 {"nome": "João", "salario": 4800, "departamento": "TI"},
]
departamentos = {}
folha_salarial = sum(sal["salario"] for sal in funcionarios)
print(folha_salarial)
maior_salario = 0
for funcionario in funcionarios:
    if funcionario["salario"] > maior_salario:
        maior_salario = funcionario["salario"]
        nome_maior = funcionario["nome"]
    departamentos[funcionario["departamento"]] = funcionario["salario"] 

print(f"O maior salário é de {nome_maior} com R${maior_salario}")
print(departamentos)

#Exercicio 4
avaliacoes = {
 "loja A": [8, 9, 7, 10, 6],
 "loja B": [5, 7, 6, 8, 7],
 "loja C": [9, 8, 9, 10, 9],
}
media_ava = {}
mediaA = sum(avaliacoes["loja A"])/len(avaliacoes["loja A"])
mediaB = sum(avaliacoes["loja B"])/len(avaliacoes["loja B"])
mediaC = sum(avaliacoes["loja C"])/len(avaliacoes["loja C"])
media_ava.append(mediaA)
media_ava.append(mediaB)
media_ava.append(mediaC)
maior_media = 0
nome_maior = ""
for loja, media in avaliacoes():
    if media > maior_media:
        maior_media = media
        nome_maior = loja
print(f"A loja com maior média é {nome_maior} com média {maior_media}")

#Exercicio 5
vendas = [
 {"vendedor": "Marcos", "itens": {"notebook": 2, "mouse": 5}},
 {"vendedor": "Lucia", "itens": {"notebook": 1, "teclado": 3}},
 {"vendedor": "Paula", "itens": {"mouse": 4, "teclado": 2}},
]
notebooks_vendidos = sum(venda["itens"].get("notebook", 0) for venda in vendas)
print(notebooks_vendidos)
melhor_vendedor = ""
mvendas = 0
for venda in vendas:
    total_itens = sum(venda["itens"].values())
    if total_itens > mvendas:
        mvendas = total_itens
        melhor_vendedor = venda["vendedor"]
print(f"O melhor vendedor é {melhor_vendedor} com {mvendas} itens vendidos")
notebooks_totais = sum(venda["itens"].get("notebook", 0) for venda in vendas)
print(f"Total de notebooks vendidos: {notebooks_totais}")
mouse_totais = sum(venda["itens"].get("mouse", 0) for venda in vendas)
print(f"Total de mouses vendidos: {mouse_totais}")
teclado_totais = sum(venda["itens"].get("teclado", 0) for venda in vendas)
print(f"Total de teclados vendidos: {teclado_totais}")

#Exercicio 6
produtos = [
 {"nome": "Notebook", "preco": 3500},
 {"nome": "Mouse", "preco": 80},
 {"nome": "Teclado", "preco": 150},
 {"nome": "Cadeira", "preco": 900},
]
preco_produtos = {}
barato = 100
caro = 1000
for produto in produtos:
    preco = produto["preco"]
    if preco < barato:
        categoria = "barato"
    elif preco > caro:
        categoria = "caro"
    else:
        categoria = "médio"
    preco_produtos[produto["nome"]] = categoria
print(preco_produtos)

#Exercicio 7
funcionarios = [
 {"nome": "Ana", "nota": 9},
 {"nome": "Carlos", "nota": 6},
 {"nome": "Beatriz", "nota": 4}, 
{"nome": "João", "nota": 7},
]
for funcionario in funcionarios:
    if funcionario["nota"] >= 8:
        situacao = "excelente"
    elif funcionario["nota"] < 5:
        situacao = "precisa melhorar"
    else:
        situacao = "regular"
    print(f"{funcionario['nome']} está com desempenho {situacao}")

#Exercicio 8
estoque = {
 "notebook": 3,
 "mouse": 25,
 "teclado": 8,
 "monitor": 2
}
for qtd in estoque:
    if estoque[qtd] < 5:
        status = "estoque critico"
    elif 5 <= estoque[qtd] <= 10:
        status = "estoque baixo"
    else:
        status = "estoque adequado"


#Exercicio 9
vendas = [
 {"regiao": "Sul", "valor": 12000},
 {"regiao": "Norte", "valor": 8000},
 {"regiao": "Sudeste", "valor": 20000},
 {"regiao": "Centro-Oeste", "valor": 5000},
]
vendas_regiao = {}
for venda in vendas:
    if venda["valor"] >= 10000:
        meta = "meta atingida"
    else:
        meta = "meta não atingida"
    vendas_regiao[venda["regiao"]] = meta
print(vendas_regiao)
    
#Exercicio 10
compras = [
    {"cliente": "Maria", "valor": 450},
    {"cliente": "José", "valor": 1200},
    {"cliente": "Clara", "valor": 3000},
]

dict_compras = {}

for compra in compras:
    valor = compra["valor"]

    if valor < 500:
        valor_final = valor * 0.95
    elif 500 <= valor <= 2000:
        valor_final = valor * 0.90
    else:
        valor_final = valor * 0.85

    print(f"{compra['cliente']} pagará R$ {valor_final:.2f}")
    dict_compras[compra["cliente"]] = valor_final

print(dict_compras)

