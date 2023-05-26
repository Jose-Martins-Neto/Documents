notas = []
soma =  0
media = 0
cont = 0

for x in range (3):
    notas.append(float(input("Digite as notas: ")))

for y in range (3):
    soma += notas[y]
media = soma / 3

for i in range (3):
    if notas[i] >= media:
        cont+=1

print(cont)

