nasc = int(input("digite seu ano de nascimento: "))
produto = int(input("digite o valor do produto: "))
idade = 2021 - nasc
desconto = (idade/produto) * 100
promocao = produto - desconto

print(f"O produto custará agora {promocao:.2f} reais")