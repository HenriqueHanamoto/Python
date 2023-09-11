# # Exercício 2:
# Dado o seguinte dicionário:
# frutas = {'maçã': 3, 'banana': 2, 'laranja': 5, 'uva': 4}
# Atualize a quantidade de uvas em seguida remova a fruta 'banana' 
# do dicionário e imprima o dicionário atualizado.

frutas = {'maçã': 3, 'banana': 2, 'laranja': 5, 'uva': 4}

new_qtd = int(input("Digite a nova quantidade de uvas:  "))
frutas["uva"] = new_qtd
del frutas["banana"]

print(frutas)