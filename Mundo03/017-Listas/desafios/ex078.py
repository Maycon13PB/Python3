valores = []
mai = 0
men = 0
for c in range(0, 5):
    valores.append(int(input(f"Digite um valor para a Posição {c}: ")))
if c == 0 :
    mai = men = valores[c]
else:
    if valores[c] > mai:
        mai = valores[c]
    if valores[c] < men:
        men = valores
print("=-" * 30)
print(f"Você digitou os valoes {valores}", end= "")
print(f"O maior valor digitado foi {mai} nas posições ", end = "")
for i, v in enumerate(valores):
    if v == mai: 
        print(f"{i}...", end="")
print()
print(f'O menor valor digitado foi {men} nas posições', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...',end='')
print()