valor = float(input("Qual e o valor da casa? R$ "))
salario = float(input("Qual e o seu salario? R$"))
anos = float(input("Em quantos  anos você quer pagar a casa"))
mensal = valor / (anos * 12 )
por =  (salario * 30 / 100)  
print("Em {:.0f} anos você ira pagar R${:.2f} por mês".format(anos, mensal))
if por <= mensal:
    print("Em felizmente você não podera finaciar a casa pois ela ecede o valor de 30% do seu salario que é de R${:.2f} ------- R${:.2f}".format(salario, por))

