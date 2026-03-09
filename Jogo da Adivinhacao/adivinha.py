import random

while True:
    print("Jogo da Adivinhação")
    print("Tente adivinhar o numero secreto entre 1 e 100.")
    print("Voce tem 3 tentativas")

    num_secreto = random.randint(1, 100)
    tentativas = 5

    while tentativas > 0:
        palpite = int(input("Digite um numero entre 1 e 100: "))
        if palpite == num_secreto:
            print("Parabens!!")
            break
        elif palpite < num_secreto:
            print("Tente um numero maior.")
        else:
            print("Tente um numero menor.")
        tentativas -= 1
        print("Tentativas restantes: " + str(tentativas))
        if tentativas == 0:
            print("Game Over! O numero era: " + str(num_secreto))
    
    op = input("Deseja jogar novamente? (s/n): ")
    if op.lower() == "s":
        num_secreto = random.randint(1, 100)
        tentativas = 5
    else:
        print("Obrigado por jogar!")
        break
    