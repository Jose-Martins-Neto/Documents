usuarios = []
senhas =[]

for x in range (2):
    usuarios.append(input("Digite o nome de um usuario: "))
    senhas.append(input("Digite a senha: "))

usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")
cont = 0

for y in range(2):
    if usuarios[y] == usuario and senhas[y] == senha:
        print("Logado com sucesso")
        break
    else:
        cont+=1
if cont == 3:
    print("Nao autorizado")