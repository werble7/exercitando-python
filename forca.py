import random


def apresentacao():

    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")


def carregar_palavra_secreta():

    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    n = random.randrange(len(palavras))
    return palavras[n]


def entrada_chute(letras_chutadas):

    chute = input("Qual letra? ")
    chute = chute.strip().lower()
    if not tratar_chute(chute, letras_chutadas):
        return False
    return chute


def tratar_chute(chute, letras_chutadas):

    if (len(chute) != 1) or (not chute.isalpha()):
        print("Chute inválido, apenas letras")
        return False
    elif chute in letras_chutadas:
        print("Você já testou essa letra!")
        return False
    else:
        letras_chutadas.append(chute)
        return True


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():

    apresentacao()
    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = ["_" for _ in palavra_secreta]
    letras_chutadas = []

    tentativas, erros = 7, 0

    enforcou = False
    acertou = False

    # enquanto não enforcou e não acertou
    while not enforcou and not acertou:

        chute = entrada_chute(letras_chutadas)
        if not chute:
            continue

        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[i] = letra
        else:
            erros += 1
            desenha_forca(erros)

        print(*letras_acertadas)
        print(f"Faltam {tentativas - erros} tentativas!")

        acertou = "_" not in letras_acertadas
        enforcou = erros == tentativas

    if enforcou:
        imprime_mensagem_perdedor(palavra_secreta)
    elif acertou:
        imprime_mensagem_vencedor()


if __name__ == '__main__':
    jogar()
