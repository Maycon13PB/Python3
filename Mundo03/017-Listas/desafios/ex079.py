números = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in números:
        números.append(n)
        print("Valor adicioanaod com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar ")
    r = str(input("Deseja continuar? [S/N]"))
    if r in "Nn":
        break
print("-=" *30)
print(f"Voce digitou os valores{números}")