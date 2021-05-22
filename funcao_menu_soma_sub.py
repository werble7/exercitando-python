
def soma_calc(a, b):
    soma = a + b
    return soma


def sub_calc(c, d):
    sub = c - d
    return sub


if __name__ == '__main__':
    retorno = 0
    print("opção 1 = soma \nopção 2 = subtração")
    opcao = int(input("digite uma opção: "))
    valor1 = int(input("valor 1: "))
    valor2 = int(input("valor 2: "))

    if opcao == 1:
        valor3 = int(input("valor 3: "))
        valor4 = int(input("valor 4: "))
        soma_calc(valor1, valor2)
        soma_calc(valor3, valor4)
        retorno1 = soma_calc(valor1, valor2)
        retorno2 = soma_calc(valor3, valor4)
        retorno = retorno1 + retorno2
    elif opcao == 2:
        sub_calc(valor1, valor2)
        retorno = sub_calc(valor1, valor2)
    else:
        print("digite uma opção válida")

    print(f"o valor é {retorno}")
