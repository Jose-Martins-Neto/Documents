alunos = int (input("Digite o numero de alunos: "))
soma = 0
x= 1

while x<=alunos:
    notas = float(input("Digite as notas: "))
    soma = soma+notas
    x=x+1

media = soma/alunos

print(media)






