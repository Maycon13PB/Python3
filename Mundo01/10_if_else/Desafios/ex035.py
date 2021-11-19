a = float(input("Digite um termo"))
b = float(input("Digite um segundo termo "))
c = float(input("Digite um terceiro termo "))
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR um triângulo")
else:
    print("Os segmentos acima NÂO PODEM FORMAR triângulo")