def somar (a,b):
    soma = a+b
    print (soma)
def subtrair (a,b):
    subt = a-b
    print(subt)
def multiplicao(a,b):
    mult = a*b
    print(mult)
def divisao (a,b):
    div = a/b
    print(div)


n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

opcao = 0

while opcao != 5:
    print('''       1 - soma
        2 - sub
        3 - mult
        4 - div
        5- sair''')

    opcao = int( input("Escolha sua opcao: "))

    if opcao == 1:
        somar (n1,n2)
    elif opcao ==2:
        subtrair(n1,n2)
    elif opcao == 3:
        multiplicao(n1,n2)
    elif opcao == 4:
        divisao(n1,n2)
    elif opcao == 5:
        print("Finalizado")
        break
    else:
        print("Numero invalido, digite novamente a opcao")
