# Exercicio 3
# Crie uma lista com algumas cores. Peça do usuário para digitar o nome de
# uma cor. Se a cor estiver na lista, permita que o usuário a substitua 
#por outra cor. Caso contrário, adicione a nova cor à lista.

N = 1
lista = ['Amarelo', 'Preto', 'Azul', 'Rosa','Roxo','Verde']

while (N == 1):
  corDigitada = input("Digite uma cor:  ")

  if corDigitada not in lista:
    lista.append(corDigitada)
    for i, Cor in enumerate(lista):
      print(i,Cor)
    break

  if (corDigitada in lista):
    subs = input("Deseja alterar a cor: Sim ou Não  ")
    if(subs == 'Sim'):
      Remover= input("Qual cor deseja remover: ")
      lista.remove(Remover)
      add = input("Qual deseja adicionar: ")
      lista.append(add)
      continue
    else:
      continue


    
    


    

