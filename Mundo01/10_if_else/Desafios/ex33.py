a = int(input("Digite um numero"))
b = int(input("DIgite outro numero"))
c = int(input("Digite outro numero"))
#Verificando quem é menor 
menor = a 
if b < a and b < c:
    menor = b 
if c < a and c < b:
    menor = c 
#Verificando que e maior 
maior = a 
if b > a and b > c:
    maior  = b 
if c > a and c > b:
    maior = c 
print("O maior numero foi \033[4;37;40m{}\033[m".format(maior))
print("O menor numero foi {}".format(menor))