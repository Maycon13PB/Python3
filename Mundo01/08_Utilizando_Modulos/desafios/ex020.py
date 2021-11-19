from random import shuffle
import random
aluno1 = str(input("Quale e o nome do primeiro aluno: "))
aluno2 = str(input("Nome do segundo aluno: "))
aluno3 = str(input("Nome do terceiro aluno: "))
aluno4 = str(input("Nome do quarto aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("A ordem sera de")
print(lista)