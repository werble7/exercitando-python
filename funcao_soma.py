
def soma_calc(a, b):
    soma = a + b
    return soma


if __name__ == '__main__':
    valor1 = float(input("valor primário: "))
    valor2 = float(input("valor secundário: "))
    valor_retorno = soma_calc(valor1, valor2)
    print(f"Soma = {valor_retorno}")
