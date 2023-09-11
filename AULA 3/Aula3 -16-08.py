"""
#===========FUNÇÕES(MODULOS)===========
#-não são clasess(classes são métodos)

# modulo some usando funções
import moduloTeste

numero1 = int(input("Informe o numero 1: "))
numero2 = int(input("Informe o numero 2: "))

resultado = moduloTeste.soma(numero1, numero2)
print(resultado)
#=======================================
#criando funções

def soma(numero1:int, numero2:int):
    total =  numero1 + numero2
    return total

numero1 = int(input("Informe o numero 1: "))
numero2 = int(input("Informe o numero 2: "))

resultado = soma(numero1, numero2)
print(resultado)
#=========================================
#importando apenas uma função de algum módulo
from moduloTeste import soma, teste

numero1 = int(input("Informe o numero 1: "))
numero2 = int(input("Informe o numero 2: "))

resultado = moduloTeste.soma(numero1, numero2)
print(resultado)
"""