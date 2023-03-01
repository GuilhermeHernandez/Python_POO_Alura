class Conta:

    def __init__(self,nmr,nome,saldo,limite):
        self.__numero = nmr
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo : R${self.__saldo} do titular {self.__nome}')

    def deposita(self,valor):
        self.__saldo += valor

    def __pode_sacar(self,valor):
        valor_disponivel_saque = self.__limite + self.__saldo
        return valor <= valor_disponivel_saque

    def saca(self,valor):

        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'Passou o limite !')

    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__nome

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    @staticmethod ### METODO STATICO N PRECISA DO OBJETO PARA RETORNA O VALOR
    def codigo_banco():
        return '001'

    @staticmethod ### METODO STATICO N PRECISA DO OBJETO PARA RETORNA O VALOR
    def codigos_bancos():
        return {'BB' : '001' , 'Caixa' : '104' , 'Bradesco' : '237'}