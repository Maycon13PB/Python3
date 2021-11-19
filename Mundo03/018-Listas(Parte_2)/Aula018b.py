galera = [["João", 19],["Ana", 33],["Joaquim", 13],["Maria", 45]]
for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade")

galera.clear()
dado = list()
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é mior de idade.")
    else:
        print(f"{p[0]} é menor de idade.")