from random import randint
contador = 0
computador = 0
num = -1
computador = randint(0, 10)# Faz o computador pega um numero
print("Sou seu computador...")
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
while num != computador:
    num = int(input("Qual e o seu palpite?"))
    if num > computador:
        print("Menos... Tente mais uma vez ")
        contador +=1
    elif num < computador :
        print("Mais... Tente mais uma vez ")
        contador +=1
print("Você acertou, Parabens!!! Você tento {} vezes para acerta".format(contador))