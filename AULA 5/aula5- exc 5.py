# Exercício 5: Substituição de Substring
# Peça ao usuário para inserir uma string e, em seguida, 
# substitua todas as ocorrências de uma substring específica por outra substring. 
# Por exemplo, substitua todas as ocorrências de "gato" por "cachorro".

Strin_g = input("Digite uma frase: ")
mudanca = input("Qual palavra deseja mudar na frase: ")
New_str = input("Digite a nova palavra: ")

Strin_g = (Strin_g.replace(mudanca, New_str))
print(Strin_g)