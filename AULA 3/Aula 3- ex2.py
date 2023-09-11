# Exercicio 2 - Loop For
# Crie um programa que peça ao usuario alguns items de compra em seguida exiba a lista

def notaFiscal(n_items:int, item:str, Compras: list):
    for i in range(0,n_items):
        item =  input("Digite o nome do item: ")
        Compras.append(item)

    print("Lista de compras:")
    for i, item in enumerate(Compras):
        print(i,item)
        
n_items = int(input("Quantos itens você deseja inserir na lista de compras? "))
Compras: list=[]
item= []

notaFiscal(n_items, Compras, item)

