dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Pesso: ")))
    if len(dados) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    if resp in "nN":
        break
print("-=" *30)
print(f"Ao todo, você cadastrou {len(pessoas)} pessoas ")
print(f"O maior peso foi de {maior}Kg.", end=" ")
for p in pessoas:
    if p[1] == maior:
        print(f"Pesso de {p[0]}",end=" ")
print()
print(f"O menor peso foi de {menor}Kg.", end=" ")
for p in pessoas:
    if p[1] == menor:
        print(f"Pesso de {p[0]}", end=" ")
print