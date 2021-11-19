ano = int(input("Digite o ano da pessoa: "))
idade =  2021 - ano
if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 20:
    print("Sênior")
else:
    print("Master")