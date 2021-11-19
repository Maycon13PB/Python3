frase = str(input("Digie uma frase qualquer: ")).strip() .strip()
print("A letra A Aparece {} vezes na frase".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A Ultima  letra A apareceu na posição {}".format(frase.rfind("A")+1))