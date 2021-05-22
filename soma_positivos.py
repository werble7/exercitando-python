soma = 0
maior = 0
menor = 10000000000000000000000

while True:
    x = int(input("digite um valor: "))
    if x < 0:
        break
    else:
        soma += x
        if x > maior:
            maior = x
        if x < menor:
            menor = x

print(f"a soma dos positivos é igual a {soma}")
print(f"o maior é {maior} e o menor é {menor}")
