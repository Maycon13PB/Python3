nota01 = float(input("Digite a primeira nota: "))
nata02 = float(input("Digite a segunda nota: "))
media = (nota01 + nata02) / 2
if media < 5:
    print("Reprovado")
elif media < 7:
    print("Recuperação")
else:
    print("Aprovado") 
