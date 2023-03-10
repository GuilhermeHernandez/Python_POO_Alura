class Cliente:

    def __init__(self,nome):
        self.__nome = nome

    @property #representa uma propriedade - n precisa fornece nenhum dado
    def nome(self):
        print(f'Chamando @propety nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self,nome):
        print(f'Chamando @nome.setter nome()')
        self.__nome = nome