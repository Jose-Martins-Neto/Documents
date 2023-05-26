x = 's'
mediaarray = []
while x == 's':

    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))

    media = (n1+n2)/2
    mediaarray.append(media)

    if media >=7:
        print("Aluno aprovado")
    elif media >=4:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")

    x = input("Deseja continuar: S/N ")

print(mediaarray)
