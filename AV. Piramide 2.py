def piramide (n):

    for x in range (n):
        for n in range (1,x+1):
            print(n, end = "")
        print()
piramide(6)