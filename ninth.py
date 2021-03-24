a = float(input("insira o valor de a: "))
b = float(input("insira o valor de b: "))
c = float(input("insira o valor de c: "))
delta = (b ** 2) - (4 * a * c)
raizdelta = delta ** 0.5
x1 = (- b + raizdelta) / (2 * a)
x2 = (- b - raizdelta) / (2 * a)
print("resultados", x1, "e", x2)



