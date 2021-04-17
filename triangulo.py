a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))
if a >= b + c:
    print("não é triângulo")
elif b >= a + c:
    print("não é um triângulo")
elif c >= a + b:
    print("não é um triângulo")
else:
    if a == b == c:
        print("isso é um triângulo equilátero")
    elif a == b != c or a == c != b or b == c != a:
        print("Isso é um triângulo isóceles")
    else:
        print("Isso é um triângulo escaleno")
