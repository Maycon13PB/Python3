import math
n = float(input("Digite o angulo que você deseja: "))
seno = math.sin(math.radians(n))
print("O seno de {} e de {:.2f}". format(n, seno))
coseno = math.cos(math.radians(n))
print("O coseno de {} e de {:.2f}". format(n, coseno))
tangent = math.tan(math.radians(n))
print("A tangente de {} e de {:.2f}".format(n, tangent))