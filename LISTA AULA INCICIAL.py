
alunos =[]
n = int(input("DIgite a quantidade de alunos: "))

for x in range(n):
    alunos.append(input("Digite o nome do aluno: "))
for y in range (n):
    print (alunos[y], y)
novo = input("Digite um novo aluno: ")
cont =0
for i in range (n):
    if novo == alunos[i]:
        print (i,alunos[i])
    else:
        cont+=1
if cont == alunos:
    print("nao encontrado")

