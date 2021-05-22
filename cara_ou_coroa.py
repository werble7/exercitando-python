import random

while True:
    jogar = input("quer jogar? ")
    if jogar == "nao":
        print("obrigado por jogar")
        break
    else:
        x = random.randint(0, 1)
        if x == 0:
            print("coroa")
        else:
            print("cara")
