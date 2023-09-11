# Exercício 1 - Estrutura condicional (if, elif, else):
# Escreva um programa que receba a idade de uma pessoa e informe 
# se ela é criança (menor de 12 anos), #adolescente (entre 12 e 17 anos)
# ou adulta (18 anos ou mais).
idade = int(input('Digite a sua idade: '))
if (idade <= 12):
    print('Criança chorando')
elif (idade > 12 and idade <= 17):
    print('Adolecente')

else:
    print ('Adulto "crescido')

    
