####################################################################

# como criar uma string ?
# '' ou ""

####################################################################

# Acessar determinado caracter:
# Podemos acessar caracteres individuais em uma string usando índices
# começando em 0 para o primeiro caractere.

# variavel = 'teste'
# print(variavel[2])

####################################################################

# Fatiando strings:
# Podemos fatiar uma string para obter uma parte específica dela,
# especificando um intervalo de índices.

# variavel = 'teste'
# print(variavel[2:4])

# [indice onde inicia: indice onde termina]

# Para reverter uma string em Python, podemos usar o conceito de "slicing" 
# com um passo negativo:

# texto = "Victor"
# texto_reverso = texto[::-1]
# print(texto_reverso)

####################################################################

# Comprimento de uma String:
# Podemos descobrir o comprimento de uma string usando a função len()

# teste = 'seu nome completo'
# print(len(teste))

####################################################################

# Concatenação de Strings:
# Podemos combinar ou concatenar strings usando o operador +:

# teste = 'ola, '
# teste2 = 'mundo'

# frase = teste + teste2
# frase = ''.join([teste, teste2])
# print(frase)

####################################################################

# Métodos de Strings:
# Python fornece vários métodos incorporados para realizar operações em strings. Alguns exemplos incluem upper() para tornar uma string maiúscula, lower() para torná-la minúscula e strip() para remover espaços em branco extras de uma string.

# texto = "   Python  teste "
# maiusculo = texto.upper()   # Isso torna a string maiúscula
# minusculo = texto.lower()   # Isso torna a string minúscula
# sem_espacos = texto.strip()  # Isso remove espaços em branco do início e do fim
# so_a_primeira_maiscula = texto.capitalize() # Somente a primeira letra em maisculo
# todas_iniciam_com_maiscula = texto.title()

# print(texto)
# print(maiusculo)
# print(minusculo)
# print(sem_espacos)
# print(so_a_primeira_maiscula)
# print(todas_iniciam_com_maiscula)

####################################################################

# Substituição
# teste = 'O mundo está girando'
# resultado = teste.replace('mundo', 'globo')
# print(resultado)