# Quando queremos importar tudo que esta em um modulo
# import modulo ( sub entendido outro arquivo )

# Quando queremos importar algo especifico de outro modulo
#from modulo import soma, teste

#def -> define uma função
# seguido pelo nome da função
# seguido por () para indicar que é executavel
    # é possivel tambem termos parametros, para isso informamos dentro de ()
# seguido por : para identificar o inicio do nosso bloco ( escopo da função )


def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return total

# É possivel retornar valores, podendo ser de quaisquer tipo
# através da palavra reservada return
# podemos retornar mais de um valor tambem, por Ex:
# return valor1, valor2

numero1 = int(input("Informe o numero 1: "))
numero2 = int(input("Informe o numero 2: "))

# para executar uma função, basta informar o nome e os ()
# caso necessário passe os parametros que seram utilizados nela
resultado = soma(numero1, numero2)
print(resultado)