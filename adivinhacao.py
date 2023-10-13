import random


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhacao!")
    print("*********************************")

    numero_secreto = random.randint(1, 101)

    while True:
        pontos = 1000
        rodada = 1
        tentativas = 0

        print("Qual o nível de dificuldade? ")
        print("(1) Fácil (2) Médio (3) Difícil")
        nivel = int(input("Defina um nível: "))

        if nivel == 1:
            tentativas = 20
        elif nivel == 2:
            tentativas = 10
        elif nivel == 3:
            tentativas = 5
        else:
            print("Digite um numero entre 1 e 3")
            continue

        for rodada in range(1, tentativas+1):
            print(f"Tentativa {rodada} de {tentativas}")
            chute = int(input("Digite um numero entre 1 e 100: "))

            if chute < 1 or chute > 100:
                print("Digite um numero entre 1 e 100!")
                continue

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if acertou:
                print("Você acertou!")
                print("Sua pontuação foi", pontos, "!")
                break
            elif maior:
                print("o seu chute foi maior que o numero secreto.")
                pontos = pontos - ((chute - numero_secreto) * nivel)
            else:
                print("o seu chute foi menor que o numero secreto.")
                pontos = pontos - ((numero_secreto - chute) * nivel)

            if pontos <= 0:
                print("Você perdeu todos os pontos!")
                pontos = 0
                break

        break

    print("Fim do jogo.", numero_secreto, "era o numero secreto!")


if __name__ == '__main__':
    jogar()
