
def minuto_hora(minutos):
    horas = minutos / 60
    return horas


def hora_minuto(horas):
    minutos = horas * 60
    return minutos


def segundo_hora(segundos):
    horas = segundos / 3600
    return horas


def hora_segundo(horas):
    segundos = horas * 3600
    return segundos


def minuto_segundo(minutos):
    segundos = minutos * 60
    return segundos


def segundo_minuto(segundos):
    minutos = segundos / 60
    return minutos


def hora_dia(horas):
    dias = horas / 24
    return dias


def dia_ano(dias):
    anos = dias / 365
    return anos


if __name__ == '__main__':
    print("Digite [0] no menu para sair:")
    print("Digite [0] no tempo para trocar a conversão e ir para o menu\n")
    menu = 1
    tempo = 1

    while menu != 0:
        print("Minutos para horas___1\nHoras para minutos___2")
        print("Segundos para horas___3\nHoras para segundos___4")
        print("Minutos para segundos___5\nSegundos para minutos___6\n")
        menu = int(input("Menu: Digite a conversão desejada: "))

        if menu == 1:
            while tempo != 0:
                tempo = int(input("Digite quantos minutos: "))
                minuto_hora(tempo)
                resultado = minuto_hora(tempo)
                print(f"Isso resulta em {resultado:0.2f} horas.")
                if tempo >= 1440:
                    hora_dia(resultado)
                    resultado2 = hora_dia(resultado)
                    print(f"Isso também resulta em {resultado2:0.2f} dias.")
                    if resultado2 >= 365:
                        dia_ano(resultado2)
                        resultado3 = dia_ano(resultado2)
                        print(f"Uau, quantos minutos para isso, {resultado3:0.2f} anos.\n")
                    else:
                        print("\n")
                else:
                    print("\n")
        elif menu == 2:
            while tempo != 0:
                tempo = int(input("Digite quantas horas: "))
                hora_minuto(tempo)
                resultado = hora_minuto(tempo)
                print(f"Isso resulta em {resultado:0.2f} minutos.\n")
        elif menu == 3:
            while tempo != 0:
                tempo = int(input("Digite quantos segundos: "))
                segundo_hora(tempo)
                resultado = segundo_hora(tempo)
                print(f"Isso resulta em {resultado:0.2f} horas.")
                if tempo >= 86400:
                    hora_dia(resultado)
                    resultado2 = hora_dia(resultado)
                    print(f"Isso também resulta em {resultado2:0.2f} dias.")
                    if resultado2 >= 365:
                        dia_ano(resultado2)
                        resultado3 = dia_ano(resultado2)
                        print(f"Uau, quantos segundos para isso, {resultado3:0.2f} anos.\n")
                    else:
                        print("\n")
                else:
                    print("\n")
        elif menu == 4:
            while tempo != 0:
                tempo = int(input("Digite quantas horas: "))
                hora_segundo(tempo)
                resultado = hora_segundo(tempo)
                print(f"Isso resulta em {resultado:0.2f} segundos.\n")
        elif menu == 5:
            while tempo != 0:
                tempo = int(input("Digite quantos minutos: "))
                minuto_segundo(tempo)
                resultado = minuto_segundo(tempo)
                print(f"Isso resulta em {resultado:0.2f} segundos.\n")
        elif menu == 6:
            while tempo != 0:
                tempo = int(input("Digite quantos segundos: "))
                segundo_minuto(tempo)
                resultado = segundo_minuto(tempo)
                print(f"Isso resulta em {resultado:0.2f} minutos.\n")
        tempo = 1

    print("Obrigado por me usar!\nAté a próxima!")
