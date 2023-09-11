# Exercício 1: 
# Crie um dicionário vazio chamado alunos e adicione três pares chave-valor 
# representando nomes de alunos e suas respectivas notas. Em seguida, calcule a média das notas.
soma = 0
M = 0.0
alunos = {
  "Galulu":5, "Marcel": 8, "Jean":10
}
qtd = len (alunos)

for a,b in alunos.items():
  soma += b
  M = soma/qtd

print('%.2f'% M)


  

  


    

  






