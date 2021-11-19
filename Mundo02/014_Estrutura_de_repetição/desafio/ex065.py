média = soma = contador = maior = menor = 0  
n = 0
r = 'S'
while r == 'S':
    n = int(input("Digite um numero"))
    contador += 1 
    soma = n + soma 
    media = soma / contador
    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    r = str(input("Você deseja continua?[S/N]")).upper().strip[0]
print("Você digitou {} vezes e a media entre todos os valores foi de {}\n O maior numero foi {} e o menor foi {}".format(contador, media, maior, menor))
