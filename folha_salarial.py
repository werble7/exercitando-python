salario_minimo = int(input("digite o salario minimo: "))
salario_m5 = salario_minimo * 5
salario_m10 = salario_minimo * 10
ct_faixa1 = 0           #salario abaixo de 5 salarios minimos
ct_faixa2 = 0           #salario entre 5 e 10 salarios minimos
ct_faixa3 = 0           #salario acima de 10 salarios minimos
folha_salarial = 0
while True:
    salario = int(input("digite o seu salario atual: "))
    if salario <= 0:
        print("nenhum dado digitado \n")
        break
    if salario < salario_m5:
        ct_faixa1 = ct_faixa1 + 1
    elif salario > salario_m5 and salario < salario_m10:
        ct_faixa2 = ct_faixa2 + 1
    else:
        ct_faixa3 = ct_faixa3 + 1
    folha_salarial = folha_salarial + salario

ct_total = ct_faixa3 + ct_faixa2 + ct_faixa1
print("quantidades de funcionários: ", ct_total)
print("folha salarial: ", folha_salarial)
print("funcionários com salário abaixo de 5 salários mínimos: ", ct_faixa1)
print("funcionários com salário entre 5 e 10 salários mínimos: ", ct_faixa2)
print("funcionários com salário maior que 10 salários minímos: ", ct_faixa3)
