numeros  = ("Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Des", "Onze", "Doze", "Treze", "cartoze", "Quinze", "Dezesseis", "Dezesete", "Dezoito", "Dezenove", "Vinte")

while True:
    num = int(input("Digite um numero entre 0 é 20: "))
    if 0 <= num <= 20:
        break
print (f"Você digitou o número {numeros[num]}")
