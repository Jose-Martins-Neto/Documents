n1 = int (input("Digite um número entre 1 e 12: "))

if n1 >= 0 and n1<12:

    if n1 == 1:
        print("O mes é janeiro")
    elif n1 == 2:
        print ("O mes digitado é fevereiro")
    elif n1 == 3:
        print ("O mes digitado é março")
    elif n1 == 4 :
        print ("O mes digitado é abril")
    elif n1 == 5:
        print ("O mes digitado é maio")
    elif n1 == 6:
        print ("O mes digitado foi junho")
    elif n1 == 7:
        print ("julho")
    elif n1==8:
        print("agosto")
    elif n1==9:
        print("setembro")
    elif n1==10:
        print("outubro")
    elif n1==11:
        print("novembro")
    else:
        print("dezembro")
else:
    print("Numero invalido")