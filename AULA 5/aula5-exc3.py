# Exercício 3: Palíndromo
# Peça ao usuário para inserir uma palavra e determine se é um palíndromo 
# (uma palavra que é a mesma se lida de trás para frente, como "radar" ou "level").

Strin = input("Digite uma Palavra: ").lower()
New = Strin[::-1]
if (Strin == New):
  print("Essa palavra é um Palíndromo")
else:
  print("Essa palavra não é um Palíndromo")
