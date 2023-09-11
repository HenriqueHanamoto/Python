# Exercício 4 - Loop while com continue e break: 
# Faça um programa que informe se o valor da compra dos items Ovos, Leite, Café e Arroz 
# atingiram o limite de 20 reais disponiveis na conta.
gasto = 0.00
dinheiro  = 20.00
item = []
#========================================================
def compras(item:str, dinheiro:float, gasto:float):
  while(dinheiro > 0):
    item = input("Qual item voce deseja comprar? ")
    if (item == 'Ovos'):
      gasto  = 3.20
      dinheiro = dinheiro - gasto
     
    if (item == 'Leite'):
      gasto  = 4.10
      dinheiro = dinheiro - gasto
        
    if (item == 'Café'):
      gasto = 4.50
      dinheiro = dinheiro - gasto       

    if (item == 'Arroz'):
      gasto  = 9.00
      dinheiro = dinheiro - gasto   

    if (dinheiro <= 0):
        print('voce não tem mais saldo')
        break 
    if (dinheiro > 0):
        print(f'Saldo restante: R$ {dinheiro:.2f}')
        print('==============================================')

        mais = input('Deseja compar mais alguma coisa ?')
        if (mais == 'sim'):
            print('==============================================')
            continue
        else:
            print('==============================================')
            print(f'Sua compra foi no valor de: R$ {20.00 - dinheiro:.2f}')
            print(f'Troco: R$ {dinheiro:.2f}')
            break
#=========================================================================================
print('=============Lista de Produtos================')
lista = [('Ovos', 'R$ 3,20'), ('Leite', '4,10'), ('Café', '4,50'), ('Arroz', '9,00')]
for nome, valor in lista:
    
    print(nome, valor)
print('==============================================')   

compras(item, dinheiro, gasto)




        
    