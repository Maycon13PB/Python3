n = int(input("Digite um numero"))
a = n % 2
b = n / n
c = n / 1 
if b == 1 and c == n and a != 0 or n == 2 :
    print("O numero {} e primo".format(n))
else:
    print("O numero {} não é primo".format(n))


num = int(input("Digite um numero: "))
tot = 0
for c in range(1, num + 1):
    if num %c == 0:
        print("\033[33m",end=' ')
        tot += 1 
    else:
        print("\033[31m", end=' ')
    print("{}".format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print("E por isso ele e PRIMO")
else:
    print("E por isso ele NÃO É PRIMO")