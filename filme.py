from sessao import Sessao


class Filme:
    def __init__(self, titulo_filme, duracao_filme, genero="Sem genero") -> None:
        self.__titulo_filme = titulo_filme
        self.__duracao_filme= duracao_filme
        self.__genero = genero

    
    @property
    def titulo_filme(self):
        return self.__titulo_filme
    
    @titulo_filme.setter
    def titulo_filme(self, valor):
        self.__titulo_filme = valor
    
    @property
    def duracao_filme(self):
        return self.__duracao_filme

    @duracao_filme.setter
    def duracao_filme(self, valor):
        self.__duracao_filme = valor

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, valor):
        self.__genero = valor
    

    def consultar_filme(self):
        return f"Nome do Filme: {self.titulo_filme}\nDuração: {self.duracao_filme}\nGenero: {self.genero}"


if __name__ == "__main__":
    f1 = Filme("Filme", 3.5)
    print(f1.consultar_filme())
    f1.genero = "sem gen"
    f1.titulo_filme = "teste"
    print(f1.titulo_filme)
