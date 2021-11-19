from datetime import date
ano = int(input("Qual e o seu nacimento"))
atual = date.today().year
idade = atual - ano 
id =  18 - idade 
if idade == 18:
    print("Já esta na hora de se alista no exercito")
elif idade > 18:
   print("Ja passou {} anos do ceu alistamento corra agora e se aliste".format(id))
else:
     print("Você ainda não pode se alista no exercito falta {} anos".format(id))