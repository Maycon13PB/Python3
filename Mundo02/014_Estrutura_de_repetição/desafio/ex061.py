inicio = int(input("Digite o inicio"))
salto = int(input("Digite o salto"))
décimo = inicio + (10 - 1) * salto
termo = 1
while inicio != décimo + salto:
    print(inicio)
    inicio = inicio + salto
while termo != 0:
    termo = int(input("Deseja acrecentar mais termos ?")) 
    if termo != 0:
        décimo = décimo + salto * termo
        while inicio != décimo + salto:
            print(inicio)
            inicio = inicio + salto  