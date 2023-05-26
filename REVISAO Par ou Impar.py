n = int(input("Digite um numero: "))

if n %2==0 and n>0:
    print("Par e positivo")
elif n %2==0 and n<0:
    print("par e negativo")
elif n%2 != 0 and n>0:
    print("impar e positivo")
else:
    print("Impar e negativo")