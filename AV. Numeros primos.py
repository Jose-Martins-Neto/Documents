def primo(n):
    if n==1:
        return  n,"nao é primo"
    elif n==2:
        return n, "é primo";
    else:
        for x in range(2,n):
            if n% x== 0:
                return n, "nao é primo"
        return n, "é primo";

print (primo (81))