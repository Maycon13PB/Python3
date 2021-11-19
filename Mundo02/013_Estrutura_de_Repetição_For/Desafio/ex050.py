soma = 0 
for c in range(1, 7):
    n = int(input("Digite um numero"))
    par = n % 2 
    if par == 0:
        soma = n + soma 
print(soma)