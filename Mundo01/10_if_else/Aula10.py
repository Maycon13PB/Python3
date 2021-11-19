nome = str(input('Qual é seu nome? '))
if nome == "Maycon":
    print("Que nome lindo você tem!")
else:
    print("Que nome mais normal!")
print("Bom dia, {}!". format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 6.0:
    print("Meus parabens você Passou")
else:
    print('Sua média foi ruim! ESTUDE MAIS')

