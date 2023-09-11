# # Exercício 5: 
# Escreva uma função que receba uma lista de números como 
# parâmetro e retorne um conjunto contendo apenas os números únicos da lista. 
# Em seguida, crie uma lista de números repetidos e teste a função com essa lista.
def lista_de_numeros(lista:list):
  n_unicos = set(lista)
  return(n_unicos)  

lista = ['1','2','5','5','6','7','8','9','9']

saida = lista_de_numeros(lista)

print(f'A lista original é {lista}')
print(f'A lista dos numeros unicos é {saida}')