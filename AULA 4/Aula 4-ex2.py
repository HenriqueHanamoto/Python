"""Exercicio 2
# Inicialize uma lista vazia. Permita que o
usuário adicione nomes de animais a essa lista até que ele insira "sair".
Em seguida, remova o último elemento da lista e exiba a lista final.
"""
lista = []
Animal = ()
N = 1
def listaAnimais(str:Animal, list:lista):
  while(N == 1):
    Animal = input("Digite o animal que deseja adicionar a lista, digite SAIR para parar: ")
    if(Animal != 'sair'):
      lista.append(Animal)
    
    if (Animal == 'sair'):
      lista.pop(len(lista) - 1)
      for i, Animal in enumerate(lista):
        print(i,Animal)
      break
  
listaAnimais(Animal,lista)
     
     