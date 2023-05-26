va = []
vm = []

for x in range (3):
    va.append(int(input("Digite os numeros: ")))

vx = int(input("Digite o valor para multiplicar: "))

for y in range(3):
    vm.append(va[y] * vx)
print (vm)
print (vx)