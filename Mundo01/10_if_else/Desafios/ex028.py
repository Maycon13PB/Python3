from random import randint
from time import sleep
computador = randint(0, 5)# Faz o computador pega um numero
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinha...")
print("-=-" * 20)
num = float(input("Digite um numero"))
print("PROCESSANDO...") # Faz o pc dormi por um tempo 
sleep(3)
if num == computador:
    print("Você acertou o numero")
else:
    print("Você errou ")
print("Eu pensei no numero {}".format(computador))