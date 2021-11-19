velocidade = int(input("Diga a velocidade que você estava: "))
if velocidade > 80:
    print("Voce ultrapassou a velocidade permitida, sera advertido")
    multa = (velocidade - 80) * 7
    print("Você pagara uma multa de {}R$".format(multa))
else:
    print("A velocidade esta de boa ")
