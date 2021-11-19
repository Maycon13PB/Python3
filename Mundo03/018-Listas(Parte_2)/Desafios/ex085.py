valor = [[], []]
for p in range(0, 8):
    numero = int(input(f"Digite o {p} valor: "))
    if numero % 2 == 0:
        valor[0].append(numero) 
    else:
        valor[1].append(numero)
print("-=" *30)
valor[0].sort()
valor[1].sort()
print(f"Os valore pares digitado foram: {valor}")
print(f"Os valores impares digitados forma {valor}")