from typing import ValuesView


valores = []
impares = []
pares = []
while True:
    valores.append(int(input("Digite um número: ")))
    resp = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if resp in "Nn":
        break
print(f"A lista completa é {valores}")
for  posi, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")