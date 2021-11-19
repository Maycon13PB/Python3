'''import math
n = float(input("Digite um numero com pontos flutuantes: "))
print("O numero {} tem parte inteira {}".format(n, math.floor(n)))'''

from math import trunc
num = float(input("Digite um valor "))
print("O valor digitado foi {}e a sua porção inteira é {}".format(num, trunc(num)))

nu = float(input("Digite um valor "))
print('O valor digitado foi {} e a sua poção inteira é {}'.format(nu, int(nu)))