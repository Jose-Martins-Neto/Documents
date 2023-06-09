import random

palavras = ['abacaxi', 'balacobaco', 'cleptomaniaco', 'banana', 'escangalhado',  'morango', 'insignificancia', 'meteorologia', 'universidade', 'serpentina', 'coledocoduodenostomia', 'dacriocistossiringotomia', 'oftalmotorrinolaringologista']

palavra_secreta = random.choice(palavras)
tamanho_palavra = len(palavra_secreta)

vidas = 6

letras_corretas = []
letras_incorretas = []

while vidas > 0:
    # Mostra a palavra com as letras corretas já descobertas
    palavra_temp = ""
    for letra in palavra_secreta:
        if letra in letras_corretas:
            palavra_temp += letra
        else:
            palavra_temp += "_"
    print(palavra_temp)

    # Mostra as letras que já foram escolhidas e estão incorretas
    print("Letras incorretas:", letras_incorretas)

    # Pede ao jogador para escolher uma letra ou digitar a palavra completa
    entrada = input("Digite uma letra ou a palavra completa: ").lower()

    # Verifica se a entrada é uma única letra
    if len(entrada) == 1 and entrada.isalpha():
        letra_escolhida = entrada

        # Verifica se a letra já foi escolhida anteriormente
        if letra_escolhida in letras_corretas or letra_escolhida in letras_incorretas:
            print("Você já escolheu essa letra antes!")
            continue

        # Verifica se a letra escolhida está na palavra secreta
        if letra_escolhida in palavra_secreta:
            letras_corretas.append(letra_escolhida)
            print("Boa escolha! A letra '{}' está na palavra secreta.".format(letra_escolhida))
        else:
            letras_incorretas.append(letra_escolhida)
            vidas -= 1
            print("Você errou! A letra '{}' não está na palavra secreta.".format(letra_escolhida))
            print("Você tem", vidas, "vidas restantes.")

    # Verifica se a entrada é a palavra completa
    elif entrada == palavra_secreta:
        letras_corretas = list(palavra_secreta)
        print("Parabéns! Você acertou a palavra secreta!")
        break

    else:
        print("Entrada inválida. Por favor, digite uma única letra ou a palavra completa.")

    print("  _____")
    print(" |/    |")
    if vidas == 6:
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
    elif vidas == 5:
        print(" |    O")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
    elif vidas == 4:
        print(" |    O")
        print(" |    |")
        print(" |")
        print(" |")
        print("_|___")
    elif vidas == 3:
        print(" |    O")
        print(" |   /|")
        print(" |")
        print(" |")
        print("_|___")
    elif vidas == 2:
        print(" |    O")
        print(" |   /|\\")
        print(" |")
        print(" |")
        print("_|___")
    elif vidas == 1:
        print(" |    O")
        print(" |   /|\\")
        print(" |   /")
        print(" |")
        print("_|___")
    else:
        print(" |    O")
        print(" |   /|\\")
        print(" |   / \\")
        print(" |")
        print("_|___")
        print("Que pena! Você perdeu. A palavra secreta era '{}'.".format(palavra_secreta))
        break

    if len(letras_corretas) == tamanho_palavra:
        print("Parabéns! Você acertou a palavra secreta!")
        break

