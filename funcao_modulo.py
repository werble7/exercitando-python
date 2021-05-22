
def modulo_calc(x):
    modulo = x
    if x < 0:
        modulo = x * (-1)
    return modulo


if __name__ == '__main__':
    valor = int(input("valor = "))
    retorno = modulo_calc(valor)
    print(modulo_calc(valor))
