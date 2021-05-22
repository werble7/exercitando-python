inicial = int(input("digite o valor inicial: "))
final = int(input("digite o valor final: "))
soma_impares = 0

if inicial > final:
    print("Não aceitamos valores inicias maiores que finais.")
else:
    for x in range(inicial, final + 1):
        if x % 2 == 1:
            soma_impares += x

print(f"a soma dos números ímpares é igual a {soma_impares}")
