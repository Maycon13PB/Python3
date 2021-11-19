valore = list()
for cont in range(0, 5):
    valore.append(int(input("Digite um valor")))
for c, v in enumerate(valore):
    print(f"Na posição {c} encontrei o alor {v}")
print("Chegei ao afinal da lista")