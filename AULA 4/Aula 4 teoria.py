"""
LISTA = [ , ]--> mutavel(è possivel adicionar dados, items[append])
Lista= [0,1,2]
V1 = Lista.pop(1[index])--> Retorna o index que foi pedido para remover;

Lista= [0,1,2,2,3]
Lista.remove(2)--> remove somente a primeira ocorrencia do item na lista;
Retorno---> 0,1,2,3


TUPLAS = ( , )--> Imutaveis, mais rapidas
"""

tupla = (1,2,3,4,5)
lista = [1,2,'produto',3,4,5,6,5,5,('teste', 2)]

#tupla imutavel
#print(tupla.count(3))#conta quantos valores existem na tupla

#lista mutavel
#append
#lista.append()#-->add items

#remove
#lista.remove(4)
#print(lista)

#pop
#index = lista.pop(7)#--> remove o item de idex 7
#print(index,lista)


#remove exemplo
#lista.remove('produto')
#print(lista)

#*Verificações com listas e tuplas

#if 'produto' in lista:
#  print("o produto está na lista")
""""
#*Compreenção de listas = List Comprehension
#tabuada
valor = int(input("Insira um valor: "))

#resultado = [valor atribuido a variavel principal---quem vou percorrer(for)---condição se houver]

resultado = [x * valor for x in range(1,11)]
print(resultado)

#tabuada execeto a do 3
valor = int(input("Insira um valor: "))
resultado = [x * valor for x in range(1,11) if x != 3]
print(resultado)"""

#conversão de tupla para lista para poder editar ela
#lista_de_tupla = list(tupla)
#print(lista_de_tupla)
"""
#função len
descobrir o tamanho da variavel ou lista

lista = [0,1,2]
V1= len(lista)"""