#Exercício 3 - Loop for utilizando a função range:
# Crie um programa que exiba a tabuada de multiplicação de um número fornecido pelo usuário. 
# O programa deve exibir a tabuada de 1 a 10.
n = int(input("Digite um numero: "))

for x in range(1, 11):
    mult = n * x
    print(f'{n} * {x} = {mult}')