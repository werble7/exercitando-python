import forca
import adivinhacao

if __name__ == '__main__':

    print("*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()
    else:
        pass
