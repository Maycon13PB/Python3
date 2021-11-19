s = contador =  0
while True:
    n = int(input("Digite um valor [999 para parar]"))
    if n == 999:
        print("Fim do progrma, Até mais")
        break
    s += n
    contador += 1
print(f"Voce digitou {contador} vezes e a soma foi de {s}")
