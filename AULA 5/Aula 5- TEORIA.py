
#Acessar determinado caracter
#podemos acessar caracteres individuais

exemplo = "olamundo"
print(exemplo[3])
"""
Fatiando Strings
Podemos facilitar uma string para obter parte especifica
especificando um intervalo de indices
[indice onde inicia: indice onde termina]

email = "faccat@faccat.com"
dominio = email[7:len(email)]
print(dominio)

Para reverter uma string em python podemos usar o : : -1

exemplo = "exemplo"
exemplo_revertido = exemplo[::-1]
print(exemplo_revertido)

Comprimento da string
print(len('exemplo'))

Concatenação de string

string1 = "olá"
string2 = "mundo"

string_real = string1 + string2
print(string_real)
--------------------------------------
string_real = ''.join(['olá ', 'mundo'])--> join junta elementos de uma lista
print(string_real)

metodos de String

exemplo = 'exemplo'
lower --> minusculo
upper--> maiusculo
title -->
strip--> remove os espaços em branco sobrando

METODO Substituição 
exemplo = 'O mundo esta girando'
novo_exemplo = exemplo.replace('mundo' , 'planeta')


"""