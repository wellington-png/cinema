class Ingresso:
    def __init__(self, codigo_assento_ingresso, tipo_ingresso, sessao=None) -> None:
        self.__codigo_assento_ingresso = codigo_assento_ingresso
        self.__tipo_ingresso = tipo_ingresso
        self.__sessao = sessao

    @property
    def tipo_ingresso(self):
        return self.__tipo_ingresso
    
    @property
    def codigo_assento_ingresso(self):
        return self.__codigo_assento_ingresso


    def gerar_ingresso(self):
        if self.__sessao.sala.capacidade_sala <= 0:
            return "Não há capacidade"
    
    def consultar_assento_ingresso(self):
        pass

    def consultar_tipo_ingresso(self):
        return self.tipo_ingresso