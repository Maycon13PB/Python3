num = [2, 5, 9, 1]
num[2] = 3
num.append(7)#append adiciona um objeto no final da lista 
num.sort(num)#sort organiza a lista
num.sort(reverse=True)#reverse organiza a lista ao contrario
num.insert(2, 0) #adiciona o numero na posição desejada
num.pop()#Elemina o paremetro escolhido  
print(num)
print(f"Essa lista tem {len(num)} elementos ")