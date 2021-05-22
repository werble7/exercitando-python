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