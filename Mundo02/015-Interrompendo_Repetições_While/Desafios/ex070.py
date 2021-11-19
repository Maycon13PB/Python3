total = maisc = d = barato = nome =  0
while True:
    print("-"*30)
    print("{: ^30}".format(" Loja baratão "))
    print("-"*30)
    produto = str(input("Nome do Produto: "))
    preço = int(input("Preço: R$"))
    print("-"*30)
    d += 1 
    total = total + preço
    if preço > 1000:
        maisc += 1
    elif d == 1 or preço < barato:
        nome = produto
        barato = preço
    cont = " " 
    while cont not in "SN":
        cont = str(input("Voce deseja continuar? [S/N]")).upper().strip()[0]
    if cont == "N":
        print("{:-^40}".format(" Fim do Programa "))
        break
print(f"O toal da compra foi de R${total:.2f}")
print(f"Temos {maisc} produto custando mais de R$1000.00")
print(f"O produto mais barato foi {nome} que custa R${barato}")