resp = "s"
while resp == "s":
    n1 = float(input("Digita a primeira nota: "))
    while n1<0 or n1>10:
        n1= float(input("Digite uma nota entre 0 e 10: "))

    n2 = float(input("Digita a segunda nota: "))
    while n2<0 and n2>10:
        n2 = float(input("Digite uma nota entre 0 e 10: "))

    media = (n1+n2)/2
    print(media)
    resp = input("Deseja continuar?")
else:
    print ("Programa finalizado")

