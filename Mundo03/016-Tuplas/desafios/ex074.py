from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Eu sortie os valores: ", end="")
for b in n:
    print(f"{b} ", end="")
print(f"\nO maior valor sorteado foi {max(n)}") #max =valor maximo 
print(f"O menor valor sorteado foi {min(n)}") #min = valor minimo 