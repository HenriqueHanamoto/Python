# Exercicio 4
# Exiba uma checklist de tarefas a fazer em um dia para o usuário,
# após isso, peça para ele dizer quais tarefas já foram concluidas,
# Exiba as tarefas que faltaram.
N = 1
lista = ['Varrer', 'colocar comida para o dog', 'Colocar água na garrafa', 
'trabalho da facul', 'vai treinar Frango']
print("===============================================")
for i, Tarefas in enumerate(lista):
  print(i,Tarefas)
#==================================================================
while(N == 1):
  print("===============================================")
  realizadas = int(input("Qual tarefa que você já realizou, Digite seu indice:  "))
  lista.pop(realizadas)
  print("===============================================")
  for i, Tarefas in enumerate(lista):
    print(i,Tarefas)
  if lista == []:
    print("Você acabou suas Tarefas")
    break
