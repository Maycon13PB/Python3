soma = 0 
cont = 0 
for c in range(1, 501, 2):
    print(c, end = ' ')
    if c % 3 == 0:
        soma = c + soma 
        cont = cont + 1 
print("A soma dos {} valores foi de {}".format(cont, soma))
