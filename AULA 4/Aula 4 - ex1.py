"""# Exercicio 1
# Crie uma lista com alguns nomes de frutas.
Peça do usuário para digitar um número de 1 a
N (onde N é o número de frutas na lista) e, em seguida, exiba 
a fruta correspondente a esse número na lista.
"""
lista_fruta= ['pera', 'pêssego', 'physalis','quina','romã','seriguela', 'sapoti','tâmara', 'tamarindo', 'tangerina']
N = int(input(f"Digite um numero de 0 a {len(lista_fruta)}:  "))

print(lista_fruta[N-1])

