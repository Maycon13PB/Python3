fazer = 4
valor1 = float(input("Digite um primeiro valor: "))
valor2 = float(input("Digite um segundo valor: "))
while  fazer != 5 :
    fazer = int(input("O que deseja fazer com esses valores?\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÙMEROS\n[5]SAIR DO PROGRAMA\n"))
    if fazer == 1:
        print("A O resultado da soma foi de {:.0f}".format(valor1 + valor2))
    elif fazer == 2:
        print("O resultado da multiplicação foi de{:.0f}".format(valor1 * valor2))
    elif fazer == 3:
        if valor1 > valor2:
            print("O maior numero foi {:.0f}".format(valor1))
        else:
            print("O maior numero foi {:.0f}".format(valor2))
    elif fazer == 4:
        print("Informes os valores novamente")
        valor1 = float(input("Digite um primeiro valor: "))
        valor2 = float(input("Digite um segundo valor: "))
    elif fazer == 5:
        print("Finalizando...")
    else:
        print("Opção invalida- Tente novamente") 
    print("Fim do programa! Volte sempre")