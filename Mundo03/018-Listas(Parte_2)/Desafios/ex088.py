from random import randint
import random
valores = []
jogos = 0
print("-"*30)
print("Joga na Mega Sena")
jogos = int(input("Quanrtos jogos você quer que eu sortei?  "))
print("SORTEANDO 10 JOGOS")
for v in range(0, jogos):
    for v in range(0, 6):
        valores.append(randint(0, 60))
    print(f"Jogo{v}:{valores}")
    valores.clear