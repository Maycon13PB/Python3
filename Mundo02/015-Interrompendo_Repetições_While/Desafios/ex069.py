idades = homens = mulheres = 0
while True:
    print("CADASTRE UMA PESSOA")
    print("-"*30)
    idade = " "
    idade = int(input("Idade: "))
    sexo = " " 
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper() .split()[0]
    print("-"*30)
    if idade >= 18:
        idades += 1
    if sexo == "M":
        homens += 1
    if sexo =="F" and idade < 20:
        mulheres += 1
    comando = " "
    while comando not in "SN":
        comando = str(input("Quer continuar? [S/N}")).upper()  .split()[0] 
    print("-"*30)
    if comando == 'N':
        print("FIM DO PROGRAMA")
        break
print(f"Total de pessoas com mais de 18 anos: {idades}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulheres} mulheres com menos de 20 anos")