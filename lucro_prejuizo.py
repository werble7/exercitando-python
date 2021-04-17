valorcompra = float(input("Digite o valor de compra: "))
valorvenda = float(input("Digite o valor de venda: "))
balanco = valorvenda - valorcompra
if balanco > 0:
    print("Você teve um lucro de ", balanco)
elif balanco < 0:
    print("Você teve um prejuízo de ", balanco)
else:
    print("Os valores são iguais, sem lucro nem prejuízo")
