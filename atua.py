class Atua:
    def __init__(self, papel_ator_filme, filme, ator) -> None:
        self.__papel_ator_filme = papel_ator_filme
        self.__filme = filme
        self.__ator = ator

    @property
    def papel_ator_filme(self):
        return self.__papel_ator_filme
    
    @papel_ator_filme.setter
    def papel_ator_filme(self, valor):
        self.__papel_ator_filme = valor