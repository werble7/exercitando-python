
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}.")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__verificar_saque(valor):
            self.__saldo -= valor
        else:
            print("Saldo insuficiente, não foi possível realizar o saque")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def __verificar_saque(self, valor):
        if valor <= self.__saldo:
            return True
        return False


if __name__ == '__main__':
    conta1 = Conta(123, "Henrique", 55.0, 1000.0)
    conta2 = Conta(321, "Gabriel", 95.0, 1000.0)
