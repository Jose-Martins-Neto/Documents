usuarios = []
senhas =[]

for x in range (1):
    usuarios.append(input("Digite o nome de um usuario: "))
    senhas.append(input("Digite a senha: "))

while True:
    f = 0
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

    for y in range(1):
        if usuarios[y] == usuario and senhas[y] == senha:
            print("Logado com sucesso")
            f = 1
            break
    if f == 1:
        break

