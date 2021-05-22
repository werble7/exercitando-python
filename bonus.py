def cara_ou_coroa():
    import random

    while True:
        jogar = input("quer jogar? ")
        if jogar == "nao":
            print("obrigado por jogar")
            break
        else:
            x = random.randint(0, 1)
            if x == 0:
                print("coroa")
            else:
                print("cara")


def soma_positivos():
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


def promocao_idade():
    nasc = int(input("digite seu ano de nascimento: "))
    produto = int(input("digite o valor do produto: "))
    idade = 2021 - nasc
    desconto = (idade / produto) * 100
    promocao = produto - desconto

    print(f"O produto custará agora {promocao:.2f} reais")


def sequencia_mil():
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


def sequencia_usuario_impares():
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


def potencia_funcao():
    def potencia(x):
        n = x ** 2
        return n

    numero = int(input("digite o numero a ser calculado: "))
    print(potencia(numero))
    print(potencia(numero) * 3)


def tabuadas():
    for n in range(3):
        if n > 0:
            print("\n")
        m = int(input("digite um numero: "))
        for y in range(1, 11):
            print(y * m)


def dez_numeros():
    print("For: ")

    print("Numeros pares: ")
    for n in range(0, 19, 2):
        print(n)

    print("\n")

    print("Numeros impares: ")
    for o in range(1, 20, 2):
        print(o)

    print("\n")

    print("While: ")

    print("Numeros pares: ")
    x = 0
    while x < 19:
        print(x)
        x += 2

    print("\n")

    print("Numeros impares: ")
    y = 1
    while y < 20:
        print(y)
        y += 2


def mencoes_media():
    m1 = int(input("digite a menção: "))
    m2 = int(input("digite a menção: "))
    m3 = int(input("digite a menção: "))

    media = (m1 + m2 + m3) / 3

    if media == 0:
        print("sua menção é SR, aluno reprovado")
    elif media > 0 and media <= 2:
        print("sua menção é II, aluno reprovado")
    elif media > 2 and media <= 4:
        print("sua menção é MI, aluno reprovado")
    elif media > 4 and media <= 6:
        print("sua menção é MM, aluno reprovado")
    elif media > 6 and media <= 8:
        print("sua menção é MS, aluno aprovado")
    elif media > 8 and media <= 10:
        print("sua menção é SS, aluno aprovado")
    else:
        print("valores incongruentes com as avaliações")

    print(f"sua media é: {media:.2f}")


def vetor_numeros():
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

# um dos exercícios está faltando, não soube fazer e o tempo não estava ao meu favor

print("-----Menu-----")
print("programas: ")
print("cara_ou_coroa___1")
print("soma_positivos___2")
print("promocao_idade___3")
print("sequencia_mil___4")
print("sequencia_usuarios_impares___5")
print("potencia_funcao___6")
print("tabuadas___7")
print("dez_numeros___8")
print("mencoes_media___9")
print("vetor_numeros___10")

while True:
    print("\n")
    print("escreva um numero fora da lista para fechar o programa.")
    x = int(input("digite qual gostaria de ver: "))
    if x == 1:
        print("\n")
        print("cara ou coroa")
        cara_ou_coroa()
    elif x == 2:
        print("\n")
        print("soma de positivos")
        soma_positivos()
    elif x == 3:
        print("\n")
        print("cálculo de promoção por idade")
        promocao_idade()
    elif x == 4:
        print("\n")
        print("sequencia 1000")
        sequencia_mil()
    elif x == 5:
        print("\n")
        print("contabilizar os impares")
        sequencia_usuario_impares()
    elif x == 6:
        print("\n")
        print("calculo de potencia")
        potencia_funcao()
    elif x == 7:
        print("\n")
        print("tabuadas de três numeros a su8a escolha")
        tabuadas()
    elif x == 8:
        print("\n")
        print("dez numeros pares e dez impares")
        dez_numeros()
    elif x == 9:
        print("\n")
        print("media das suas notas")
        mencoes_media()
    elif x == 10:
        print("\n")
        print("vetores na lista")
        vetor_numeros()
    else:
        print("digite algum dos numeros da lista")
        break
