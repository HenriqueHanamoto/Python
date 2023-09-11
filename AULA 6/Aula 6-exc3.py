# Exercício 3: 
# Crie um programa que peça ao usuário para digitar uma frase e conte 
# a frequência de cada palavra na frase. 
# Armazene as palavras e suas frequências em um dicionário e imprima o resultado.
frase = input("Digite uma frase: ")

frase = frase.lower()
frase = frase.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
Palavras = frase.split()

frequencias = {}
palavra = str

for palavra in Palavras:
  if palavra in frequencias:
    frequencias[palavra] += 1
  else:
    frequencias[palavra] = 1

print("Frequência das palavras na frase:")
for palavra, frequencia in frequencias.items():
  print(f"{palavra}: {frequencia}")

