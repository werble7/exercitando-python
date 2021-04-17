genero = int(input("Digite seu gênero, se for homem 1, mulher 2: "))
if genero == 1:
    altura = float(input("digite sua altura em metros: "))
    pesoideal = (72.7 * altura) - 58
    print(pesoideal)
else:
    altura = float(input("digite sua altura em metros: "))
    pesoideal = (62.1 * altura) - 44.7
    print(pesoideal)
