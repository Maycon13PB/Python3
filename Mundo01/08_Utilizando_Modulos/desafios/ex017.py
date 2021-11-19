'''adjacente = float(input("Digite o tamnho do cateto adjacente: "))
oposto = float(input("Digite o tamnho do carteto oposto: "))
hipotenusa = (adjacente ** 2 + oposto ** 2 ) ** (1/2)
print("A hipotenusa vai medi {:.2f}".format(hipotenusa))'''

import math
co = float(input("Digite o cateto adjacente: "))
ca = float(input("Digite o comprimento do cateto adjacente"))
h1 = math.hypot(co ,ca)
print("a hipotenusa e de {:.2f}".format(h1))