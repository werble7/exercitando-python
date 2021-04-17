a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b; "))
c = int(input("Digite o valor de c: "))
delta = (b ** 2) - (4 * a * c)
if delta < 0:
    print("conjunto vazio ou não divide por 0")
else:
    if a == 0:
        print("não divisível por zero")
    elif delta == 0:
        x = - b / (2 * a)
        print(x)
    else:
        raizdelta = delta ** 0.5
        x1 = (- b + raizdelta) / (2 * a)
        x2 = (- b - raizdelta) / (2 * a)
        print(x1, "e", x2)
