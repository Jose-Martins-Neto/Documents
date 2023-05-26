ope = 0

while ope != 6:
    n1 = int(input("Digite o primeiro numero:"))
    n2 = int(input("Digite o segundo numero numero:"))

    while True:

        print ("1 soma")
        print ("2 subtracao")
        print ("3 multiplicacao")
        print ("4 divisao")
        print ("5 digite outro numero:")
        print ("6 para sair ")

        ope = int(input("Digite a opcao: "))
        soma = n1 + n2
        sub = n1 - n2
        mult = n1 * n2
        div = n1 / n2
        if ope == 1:
            print(soma)
        elif ope == 2:
            print(sub)
        elif ope == 3:
            print(mult)
        elif ope == 4:
            print(div)
        elif ope == 5:
            break
        elif ope == 6:
            print("Programa encerrado: ")
            break
