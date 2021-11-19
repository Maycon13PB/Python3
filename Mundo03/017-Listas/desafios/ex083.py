cont1 = cont2 = 0
expre = (str(input("Digite uma expressão: ")))
for i, v in enumerate(expre):
    if v == '(':
        cont1+=1
    elif v ==')':
        cont2+=1
if cont1 == cont2:
    print("Sua expressão está correta")
else:
    print("Sua expressão está errada")
print(f"Bah {expre.count(')')}")
