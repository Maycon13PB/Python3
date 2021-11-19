Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0] ]
spr = mai= scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        Matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]"))
print("-="*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{Matriz[l] [c]:^5}]", end='')
        if Matriz[l][c] % 2 ==0:
            spr += Matriz[l][c]
    print()
print("-=" *30)
print(f"A soma dos valores pares é {spr}")
for l in range(0, 3):
    scol += Matriz[l][2]
for c in range(0, 3):
    if c == 0:
        mai = Matriz[l][c]
    elif Matriz[l][c] > mai:
        mai = Matriz[1][c]
print(f"O maior valor da segunda linha é {mai}") 