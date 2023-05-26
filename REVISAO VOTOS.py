eleitores = float(input("Digite o numero de eleitores:"))

branco = float(input("Digite os votos em branco: "))
valido = float(input("Digite os votos validos: "))
nulo = float(input("Digite os votos nulos: "))

brancos = (eleitores*branco)/100

nulos = (eleitores*nulo)/100

validos =



print("Votos em Brancos" , brancos)
print("Votos nulos" , nulos)
print("Votos em Validos" , validos)