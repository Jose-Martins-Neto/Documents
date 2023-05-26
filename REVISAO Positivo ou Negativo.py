valores = []
x = 's'
while x == 's':

    n = float(input("Digite um numero: "))

    if n >= 0:
        print("Valor positivo")
    else:
        print("Valor negativo")
    x = input("Deseja continuar? S/N : ")