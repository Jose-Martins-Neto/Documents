v = []
vpar = []

for x in range(5):
    v.append(int(input(("Digite um numero: "))))



for y in range(5):
    if v[y] %2 == 0:
        vpar.append(v[y])

menor = v[0]
maior = v[0]
soma = 0
cont= 0

for z in range (5):
    if v[z] < menor:
        menor = v[z]

    if v[z] > maior:
        maior = v[z]

for a in range(5):
    soma+= v[a]
media = soma/5

for t in range(5):
    if v[t] > media:
        cont+=1



print("numeros pares", vpar)
print(f"O maior valor digitado {maior}")
print(f"Menor valor digitado {menor}")
print(f"Valores que sao maior que a média {cont}")