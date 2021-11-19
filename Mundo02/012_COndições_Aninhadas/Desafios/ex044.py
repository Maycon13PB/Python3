produto = int(input("Qual é o valor do produto:? "))
modo = int(input("Digite 1 para pagamento avista ou cheque: \n Digite 2 para pagamento avista no cartão: \n Digite 3 para pagamento em 2x no cartão: \n Digite 4 para pagamento no cartão em 3x ou mais: \n ---->"))
if modo == 1:
    print("Preço do produto com desconto ficara em{:.2f}R$".format(modo - modo * 10 / 100))
elif modo == 2:
    print("O preço do produto ficar {:.2f}R$ com o desconto".format(modo - (modo * 5) / 100))
elif modo == 3:
    print("Oproduto ficara em {:.2f}R$".format(produto))
else:
    print("O produto ficara em {:.2f}R$".format(modo + (modo * 20) / 100))