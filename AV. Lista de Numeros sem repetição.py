def listas (lst):
    b = []

    for num in lst:
        if num not in b:
            b.append(lst)
        print(b)


a= [1,2,2,3,4,5,4,6,7]
listas (a)