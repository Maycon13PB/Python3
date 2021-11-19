viagem = float(input("Digite a ddistancia da sua viagem: "))
if viagem > 200:
    valor = viagem * 0.45
    print("O valor da passagem sera de \033[1;30m{:.2f}R$\033[m".format(valor))
else:
    valor = viagem * 0.50
    print("O valor da passagem sera de \033[0;32m{:.2f}R$\033[m".format(valor))
