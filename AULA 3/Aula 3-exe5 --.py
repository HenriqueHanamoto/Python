import random
jogar: str("jogar")

def jogo():
    aleatorio = random.randint(1, 100)
    acertou = False

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while not acertou:
        tentativa = int(input("Digite seu palpite: "))
        if tentativa == aleatorio:
            acertou = True
            print("Parabuainss! Você acertou o número")
        elif tentativa < aleatorio:
            print("O número é maior, tente novamente.")
        else:
            print("O número é menor, tente novamente.")

if "jogar" == "jogar":
    jogo()
  