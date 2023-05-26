soma = 0
x=1
while x<=3:
    num = float(input("Digite o numero:"))
    soma = soma+num
    x=x+1 #contador, x( que o valor inicial é 1 vai ser somado a 1 até chegar na condição (3) para poder parar )

media = soma/3

print(media)