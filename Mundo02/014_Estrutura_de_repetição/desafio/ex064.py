n = somador = contador = 0
n = int(input("Digite um numero [999 para parar]"))
while n != 999:
    n = int(input("Digite um numero [999 para parar]"))
    somador = somador + n
    contador +=1
print("Você digitou {} vezes e soma ao total foi de {}".format(contador, somador -999 ))