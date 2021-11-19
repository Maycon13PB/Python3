frase = "Curso em Vidéo Python"
print(frase[:13:2]) #O primeiro termo mostra o inico onde deve começa a mostra as letras da frase o segundo mostra o fina e o terceiro o espaçamento

print(frase.count("o"))#Conta quantas vezes tem o o na frase
print(len(frase))#Mostra o tamanho da frase 

print(len(frase.strip()))#Remove os espaços indesejado antes e depois  OBs:se colocar r na frente de strip vai remove so os espaço da direita e se por l remove da esquerda

print(frase.replace('Python','Android'))#Troca a palavra do primeiro termo pela a segunda 

print('Curso' in frase)#Mostra se a palavra esta dentro do da frase retornado sim ou não 

print(frase.find('Curso'))#Mostra a colocação da Palavra 

print(frase.split())#Faz a palavra vira uma lista tirando o espaçameto

print('-'.join(frase))#Junta as palavras com o objeto definido 

print(frase.upper()) #upper joga todas as palavras em letra maiúsculas 

print(frase.lower())#lower joga todas as palavras em minusculas 

print(frase.capitalize())#Joga todas as palavras em minuscula e so a primeira fica em maiuscula 

print(frase.title())#Joga todas as palavras de inicio de frase em maiuscula

print(frase.find())#Serve para encontra o primeira letra 

print(''.join(frase))#Junta todas as palavras com o que tem dentro do parentes 
