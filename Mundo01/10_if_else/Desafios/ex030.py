num = int(input("Digite um numero: "))
resultado = num % 2 
if resultado == 0:
    print("O numero \033[4;33m{}\033[m e par".format(num))
else:
    print("O numero \033[4;35m{}\033[m e impar".format(num)) 