lanche = ("Hsmbúrguer", "Suco", 'Pizza', 'Pudim')
# Tuplas são imutáveis
print(lanche)[1]
print(lanche)[3]
print(lanche)[-2]
print(lanche)[1:3]
print(lanche)[2:]
print(lanche)[:2]
print(lanche)[-2:]

for cont in range(0, len(lanche)):#len serve par falar  o que esta dentro da variavel
    print(lanche [cont])#O conte nese caso serve para mostra a colocação

for comida in lanche:
    print(f"Eu vou comer {comida}")

for pos, comida in enumerate(lanche):# enumerate serve para enumera a ordem 
    print(f"Eu vou comer {comida} na posição {pos}")
print("Comi pra caramba!")

print(sorted(lanche))#sorte ponha em ordem o que esta na var 
