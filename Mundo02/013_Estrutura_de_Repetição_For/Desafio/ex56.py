controle = 0 
menor = 20
pessoas = 0
media = 0
for c in range(1, 5):
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade da pessoa: "))
    sexo = int(input("Digite  [1] para o sexo masculino e [2] para femenino: "))
    media = idade + media 
    if idade > controle and sexo == 1:
        controle = idade
        velha = nome 
    elif idade < 20 and sexo == 2:
        pessoas = pessoas + 1 
print("A media do grupo e de {:.0f}".format(media / 4))
print("O Homem mais velho do grupo é o {}".format(velha))
print("E tem {} mulhere menor de 20 anos".format(pessoas))