altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
imc = peso / (altura * altura) 
if imc < 18.5:
    print("Abaixo do Peso")
elif imc < 25: 
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("OBesidade")
else:
    print("Obesidade móbida")