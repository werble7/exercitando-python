
class Data:
    def __init__(self, dia, mes, ano):
        if dia < 32 or mes < 13:
            self.dia = dia
            self.mes = mes
            self.ano = ano
        else:
            print("Data inválida, valores ajustadas para 01/01/2001")
            self.dia = 1
            self.mes = 1
            self.ano = 2001

    def formatada(self):
        print(f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}")


if __name__ == '__main__':
    d = Data(27, 11, 2021)
    d.formatada()
