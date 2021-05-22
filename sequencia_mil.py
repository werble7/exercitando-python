print("digite [1000] para sair.")
total = 0
total_par = 0

while True:
    x = int(input("digite um valor: "))
    if x == 1000:
        print("Obrigado por me usar!")
        break
    elif x % 2 == 0:
        print("Numero par")
        total_par += 1
    else:
        print("Numero impar")
    total += 1

print(f"O total de numeros é de {total}")
print(f"O nuemro de pares é de {total_par}")
