a = float(input("insira o valor de a: "))
b = float(input("insira o valor de b: "))
c = float(input("insira o valor de c: "))
delta = (b ** 2) - (4 * a * c)
if delta == 0:
    x1 = -b / (2 * a)
    print(x1)
elif delta < 0:
    print("equação de conjunto vazio")
else:
    raizdelta = delta ** 0.5
    x1 = (- b + raizdelta) / (2 * a)
    x2 = (- b - raizdelta) / (2 * a)
    print("as raízes são", x1, "e", x2)
