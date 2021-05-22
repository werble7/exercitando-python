
def soma_calc(a, b):
    soma = a + b
    return soma


def sub_calc(c, d):
    sub = c - d
    return sub


if __name__ == '__main__':
    valor1 = int(input("valor 1: "))
    valor2 = int(input("valor 2: "))
    soma_retorno = soma_calc(valor1, valor2)
    sub_retorno = sub_calc(valor1, valor2)
    print(f"a soma é de {soma_retorno} e a subtração é de {sub_retorno}")
