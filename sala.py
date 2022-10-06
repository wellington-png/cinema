from assento import Assento


class Sala:
    def __init__(self, numero_sala, capacidade_sala, assento) -> None:
        self.__numero_sala = numero_sala
        self.__capacidade_sala = capacidade_sala
        self.__assentos = [*assento]

    @property
    def capacidade_sala(self):
        return self.__capacidade_sala
    
    @capacidade_sala.setter
    def capacidade_sala(self, valor):
        self.__capacidade_sala = valor

    @property
    def numero_sala(self):
        return self.__numero_sala

    @property
    def assentos(self):
        return [x.codigo_assento for x in self.__assentos]
    
    def consultar_sala(self):
        return len(self.__assentos)

assent1 = Assento("Cod-200")
assent2 = Assento("Cod-300")
assent3 = Assento("Cod-400")

sala = Sala(100, 10, [assent1, assent2, assent2])
print(sala.assentos)