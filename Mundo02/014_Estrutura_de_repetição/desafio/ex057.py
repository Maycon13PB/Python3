sexo = str(input("Digite M para sexo masculino e F para femenino: ")).upper().strip()[0]
while sexo not in 'MmFf':
    print("Você errou na digitação digite navamente")
    sexo = str(input("Digite M para sexo masculino e F para femenino: ")).upper()
print("Sexo {} registrado com sucesso".format(sexo))