# Exercício 4 - Loop while com continue e break: 
# Faça um programa que informe se o valor da compra dos items Ovos, Leite, Café e Arroz 
# atingiram o limite de 20 reais disponiveis na conta.
#======================funções===========================
def carteira(dinheiro:float):
  if(dinheiro > 0):
    continuar = 1
    return continuar
    
  if(dinheiro == 0):
    continuar = 0
    return continuar

def compras(item:str, dinheiro:float, gasto:float):
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

  return(dinheiro, gasto)    
#===========================variaveis=======================
gasto = 0.00
dinheiro = 20.00

#==========================PROGRAMA=============================

print('=============Lista de Produtos================')
lista = [('Ovos', 'R$ 3,20'), ('Leite', '4,10'), ('Café', '4,50'), ('Arroz', '9,00')]
for nome, valor in lista:
    
    print(nome, valor)
print('==============================================')   

prosseguir = carteira(dinheiro)
#------------------------------------------
if (prosseguir == 0):
    print('voce não tem mais saldo')
#------------------------------------------ 
else:
  while(prosseguir == 1):
    item = input("Qual item voce deseja comprar? ")
    
    dinheiro_restante, dinheiro_gasto  = compras(item, dinheiro, gasto)

    if (dinheiro_restante > 0):
        print(f'Saldo restante: R$ {dinheiro_restante:.2f}')
        print('==============================================')

        mais = input('Deseja compar mais alguma coisa ?')
        if (mais == 'sim'):
            print('==============================================')
            dinheiro_restante = dinheiro_restante + dinheiro_restante
            continue
        else:
            print('==============================================')
            print(f'Sua compra foi no valor de: R$ {dinheiro_gasto:.2f}')
            print(f'Troco: R$ {dinheiro_restante:.2f}')
            break


