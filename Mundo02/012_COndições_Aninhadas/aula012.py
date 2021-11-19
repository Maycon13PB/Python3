from typing import Protocol


nome = str(input("Qual e o seu nome?"))
if nome == "Gustavo":
    print("Que nome mais bunito")
elif nome == "Pedro" or nome == "Maycon" or nome == "Maria":
    print("Seu nome é bem popular no Brasil.")
else:
    print("Sue nome e bem normal.")
print("Tenha um bom dia, {}!".format(nome))
