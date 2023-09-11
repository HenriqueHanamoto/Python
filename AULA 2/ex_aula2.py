# Exercício 1 - Estrutura condicional (if, elif, else):
# Escreva um programa que receba a idade de uma pessoa 
# e informe se ela é criança (menor de 12 anos), 
# adolescente (entre 12 e 17 anos)
# ou adulta (18 anos ou mais).

# idade = int(input("Informe sua idade: "))
# if idade < 12:
#     print("Voce é criança")
# elif idade >= 12 and idade <= 17:
#     print("Voce é adolescente")
# else:
#     print("Voce é adulto")

# Exercicio 2 - Loop For
# Crie um programa que peça ao usuario alguns 
# items de compra em seguida exiba a lista

# itens_pedido = []
# for itens in range(1,6):
#     item = input(f"Informe o item de numero {itens}: ")
#     itens_pedido.append(item)

# for itens in itens_pedido:
#     print(itens)


# Exercício 3 - Loop for utilizando a função range:
# Crie um programa que exiba a tabuada de multiplicação 
# de um número fornecido pelo usuário. 
# O programa deve exibir a tabuada de 1 a 10.

# numero = int(input("Informe um numero"))

# for idx in range(1, 11):
#     total = idx * numero
#     print(f"{idx} X {numero} = {total}")

# Exercício 4 - Loop while com continue e break: 
# Faça um programa que informe se o valor da compra 
# dos items Ovos, Leite, Café e Arroz 
# atingiram o limite de 20 reais disponiveis na conta.

# def exibe_lista_de_produtos(GONDULA):
#     for idx, item in enumerate(GONDULA):
#         print(f"{idx} - {item[0]}: {item[1]}")

# SALDO_CARTEIRA = 20.00
# GONDULA = [("ovos 12", 7.59), ("leite", 4.99), ("Café", 9), ("Arroz 1kg", 11.10)]

# compras_realizadas = []

# print("Bem vindos ao mercado Dia a Dia, o que deseja comprar: ")
# exibe_lista_de_produtos(GONDULA)

# item = int(input("Digite o numero do item que deseja: "))
# compras_realizadas.append(item)

# deseja_continuar = int(input("Deseja continuar comprando? 1.SIM 2.Não:"))

# if deseja_continuar == 1:

#     continua = True
#     while continua:
#         exibe_lista_de_produtos(GONDULA)

#         item = int(input("Digite o numero do item que deseja: "))
#         valor_item_compra = GONDULA[item][1]
#         total = 0

#         for item_compra in compras_realizadas:
#             total += GONDULA[item_compra][1]

#         total += valor_item_compra
#         if total >= SALDO_CARTEIRA:
#             print("Voce ja atingiu o limite da carteira.")
#             continua = False
#             break
#         else:
#             compras_realizadas.append(item)
#             continue

# else:
#     print("Obrigado pela compra")

# Extra -----------------------------------------------------------------------

# Exercício 5 - Loop while:
# Faça um programa que peça ao usuário para adivinhar 
# um número entre 1 e 100. 
# O programa deve gerar um número aleatório e informar
# se o usuário acertou, errou ou se o número é maior 
# ou menor.