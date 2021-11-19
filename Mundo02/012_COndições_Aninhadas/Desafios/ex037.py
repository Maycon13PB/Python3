num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para coversão 
[1] converte para BINARío
[2] converte para octal
[3] converte para hexadecimal''')
opcao = int(input("Sua opção"))
if opcao ==1:
    print("{} converido para BINÁRIO é ingual a {}".format(num, bin(num)))
elif opcao == 2:
    print("{} convertido para octal é ingual a {}".format(num, oct(num)))
elif opcao == 3:
    print("{} convertido para hexadecimal é ingual a {}".format(num, hex(num)))
else:
    print("Opção errada")