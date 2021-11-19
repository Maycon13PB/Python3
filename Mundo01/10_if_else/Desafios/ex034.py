salario = float(input("Qual e o seu salario"))
if salario <= 1250.00:
    reajuste = (salario * 10 / 100) + salario
else:
    reajuste = (salario * 15 / 100) + salario
print("O reajuste sera de \033[0;32;40m{:.2f}R$\033[m".format(reajuste))
 