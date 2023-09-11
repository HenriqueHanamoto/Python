""" operadores de atribuição
 ==, +=, -=, *=

teste = 20
teste += 10(

Lista .append()---> add valores a listas
teste: list = []
teste.append(20)
teste.append('teste')

ESTRUTURAS CONDICIONAIS
-if
  if not true ou true:
    print('ola')

-elif(senão se)
  elif 'teste' == 'teste':
    print ('teste')
-else
  else:
    print('else')

*Loop While
teste = False
contador = 10
while(contador >= 0):
    print(contador)
    contador -= 1
*Loop For
lista: list = [0,1,2,3]
for n in lista:
    print(n)
--------------
lista = [('nome', 'Victor'), ('nome', 'Pedro'), ('nome', 'Henrique')]
for nome, valor in lista:
    print(nome, valor)

*Loop com continue e break
lista = ['Maria','josep', 'paulo']
for nome in lista:
    if nome == 'paulo':
        break
    else:
        print(nome)
        continue
*Loop com a função range()
for x in range(0(start),101(stop), 10(step)):
    print(x)

#*função enumerate()---> mostra os índices das listas
lista = ['valor1','valor2', 'valor3']
for item in enumerate(lista):
    print(lista[item[0]])
--------------------------------------
#for index, valro in enumerate(lista):
#   print(lista[index])
------------------------------------------
*Função randrange do modulo random
import random
valor = random.randrange(0,11)
  print(valor)
"""
