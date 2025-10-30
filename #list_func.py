#list_func
#parte 1
#Exercicio 1
func1 = lambda x:x**2
func1(4)

#Exercicio 2
func2 = lambda x: 5*x - 3
func2(2)

#Exercicio 3
func3 = lambda x: x**2 + 2*x + 1
func3(-1)
func3(0)
func3(1)

#Exercicio 4
func4 = lambda x,y: x**2 + 2*x*y + y**2
func4(2,4)

#Exercicio 5
func5 = lambda x,y,z: x**y + z
fuunc5(3,2,10)

#parte 2 
#exercicio 6
def lucro(Receita, Custo):
    return Receita - Custo
lucro(10000,7500)

#exercicio 7
def margem_lucro(receita, custo):
    Margem = (lucro/receita)*100
    return Margem
margem_lucro(20000,15000)

#exercicio 8
def ponto_equilibrio(custo_fixo,preco,custo_variavel):
    Qe = custo_fixo/(preco - custo_variavel)
    return Qe
ponto_equilibrio(5000,50,30)

#exercicio 9
def folha(funcionarios):
    for salarios in funcionarios:
        salario = salarios["salario"]
        folha_salarial = sum(salario)
    return sum(funcionarios["salario"])
folha([{"nome":"Ana","salario":3000},{"nome":"Carlos","salario":4500}])

#Exercicio 10
def juros_compostos(capital, taxa, tempo):
    montante = capital * (1+i)**tempo
    juros_compostos(1000,0.02,12)
    return montante