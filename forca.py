import random
banco_palavras = ["sorvete", "marralo", "morango"]
chances = 4
letra_guardada = []
ganhou = False
palavra = random.choice(banco_palavras)

while True:
    for x in palavra:
        if x in letra_guardada:
            print (x, end=" ")
        else:
            print("_", end=" ")
    print(f"Voce tem {chances} chances")
    letra_chutada = input("Digite uma letra: ")
    letra_guardada.append(letra_chutada)
    if letra_chutada not in palavra:
        chances -=1

    ganhou = True
    for x in palavra:
        if x not in letra_guardada:
            ganhou = False

    if chances==0 or ganhou:
        break
if ganhou:
    print(f"Voce GANHOU. A palavra era {palavra} : ")
else:
    print(f"Voce PERDEU. A palavra era {palavra} : ")