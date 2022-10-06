class Ator:
    def __init__(self, nome_ator) -> None:
        self.__nome_ator = nome_ator

    @property
    def nome_ator(self):
        return self.__nome_ator

    @nome_ator.setter
    def nome_ator(self, valor):
        self.__nome_ator = valor