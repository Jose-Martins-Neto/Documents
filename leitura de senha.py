x=str (25)
senha = str(input("Digite uma senha:"))
i = 0

while senha != x:
   print("Senha incorreta")
   senha = str(input("Digite uma senha:"))
   i+=1
   if i>=2:
       print("Senha bloqueada")
       break
else:
    print("Senha correta")
