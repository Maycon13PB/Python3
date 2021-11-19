a = float(input("Digite um termo"))
b = float(input("Digite um segundo termo "))
c = float(input("Digite um terceiro termo "))
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR um triângulo ", end='')
    if a == b and b ==c:
        print("Equilatero")
    elif a != b != c != a:
        print("Escaleno")
    else:
        print("Isoceles")
else:
    print("Os segmentos acima NÂO PODEM FORMAR triângulo")