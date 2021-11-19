inicio = int(input("Digite o inicio"))
salto = int(input("Digite o salto"))
décimo = inicio + (10 - 1) * salto
for c in range(inicio, décimo + 1, salto):
    print(c)