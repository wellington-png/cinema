class Genero:
    def __init__(self, descricao_genero) -> None:
        self.__descricao_genero = descricao_genero
        
    @property
    def descricao_genero(self):
        return self.__descricao_genero
    
    def __str__(self) -> str:
        return self.descricao_genero


if __name__ == "__main__":
    gen = Genero('Hello')
    print(gen)