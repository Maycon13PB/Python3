from datetime import date
soma1 = 0 
soma2 = 0
for c in range(1,7):
    ano = int(input(("Digite o ano de nacimento:")))
    data = date.today().year
    idade =   data - ano
    if idade >= 18:
        soma1 = soma1 + 1
    else:
        soma2 = soma2 + 1 
print("Dos anos digitados {} são maiores e {} são menore ".format(soma1, soma2))
