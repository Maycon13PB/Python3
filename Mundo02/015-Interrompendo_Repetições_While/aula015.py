n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
#print("A soma vale {}".format(s))
print(f"A soma vale {s}") #PYTHON 3.6+


nome = "Jose"
idade = 33
print(f"O {nome} tem {idade} anos ")#PYTHON 3.6+
print("O {} tem {} anos ".format(nome, idade))#PYTHON 3
print(f"O %s tem %d anos " % (nome, idade))#PYTHON 2
