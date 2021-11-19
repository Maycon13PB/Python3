from random import randint
from time import sleep
intens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print('''ESCOLHA
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
print("JA")
sleep(1)
print("KeN")
sleep(1)
print("PO!!!")
print("-=-" * 20)
print("Computador escolheu {}".format(computador))
print("Jogador escolheu {}".format(jogador))
print("-=-" * 20)
if computador == 0:
    if jogador == 0:
        print("Empate")
    elif jogador == 1: 
        print("Jogador vence")
    elif jogador ==2:
        print("Computador vence")
    else:
        print("Jogada invalida")
elif computador == 1:
    if jogador ==0:
        print("Computador Vence")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2: 
        print("Jogador vence")
    else: 
        print("Jogada invalida")
elif computador == 2:
    if jogador == 0:
        print("Jogador vence")
    elif jogador == 1:
        print("Computador vence")
    elif jogador == 2:
        print("Empate")
    
    else:
        print("Jogada invalida")