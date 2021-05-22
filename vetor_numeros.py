numeros = []
total = 0

z = int(input("quantos numeros você quer por na lista? "))
for n in range(z):
    x = int(input("digite valores para a lista: "))
    numeros.append(x)

print(len(numeros))
print(numeros)
numeros[4] = 100
print(numeros)
