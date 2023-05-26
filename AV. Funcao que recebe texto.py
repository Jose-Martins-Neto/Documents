def textolouco (texto):
    letras = 0
    textoinvertido = " "

    for letra in range (len(texto)-1,-1,-1):
        textoinvertido += texto[letra]

        if letra != " ":
            letra+=1
    return letras, textoinvertido

resp = textolouco ('joaoa e maria')
print (resp)