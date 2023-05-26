def somar (a,b):
    return a+b
def subtrair (a,b):
    return a-b
def multiplicao(a,b):
    return a*b
def divisao (a,b):
    return a/b
def estoque (nome,q,valor):
    total = q * valor
    return nome, total
def somar (*num):
    s = 0
    for x in num:
        s+= x
    return s

def primo(n):
    if n==1:
        return  n,"nao é primo"
    elif n==2:
        return n, "é primo";
    else:
        for x in range(2,n):
            if n% x== 0:
                return n, "num é primo"
        return n, "é primo"
