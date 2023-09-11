# Exercício 1: Contagem de Vogais
# Escreva um programa que peça ao usuário para inserir uma string e
# em seguida, conte o número de vogais (a, e, i, o, u) nessa string.

String = input("Digite uma frase qualquer:  ")
String.lower()

lista_vogal = ['a','e','i','o','u']
lista = []
qtd = 0

for i in String:
  if i in lista_vogal:
    lista.append(i)
    qtd += 1

print(f'A quantidade de vogais é {qtd}')

    


    

