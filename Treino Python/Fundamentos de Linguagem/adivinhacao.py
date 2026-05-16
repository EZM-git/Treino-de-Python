import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while tentativas < 10 and not acertou:
        palpite = int(input("Qual seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print("Você acertou o número parabéns!")
            acertou = True
        elif palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        else:
            print("Muito alto! Tente novamente.")
    else:
        print(f"O número secreto era: {numero_secreto}")

if __name__ == "__main__":
    jogar()