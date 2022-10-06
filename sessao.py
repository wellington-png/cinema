class Sessao:
    def __init__(self, data_sessao, hora_sessao, valor_inteira, valor_meia, sessao_encerrada, filme, ingressos=[]):
        self.__data_sessao = data_sessao
        self.__hora_sessao = hora_sessao
        self.__valor_inteira = valor_inteira
        self.__valor_meia = valor_meia
        self.__sessao_encerrada = sessao_encerrada
        self.__ingressos = [*ingressos]
        self.__filme = filme


    
    @property
    def data_sessao(self):
        return self.__data_sessao

    @property
    def hora_sessao(self):
        return self.__hora_sessao

    @property
    def valor_inteira(self):
        return self.__valor_inteira
    
    @property
    def valor_meia(self):
        return self.__valor_meia
    
    @property
    def sessao_encerrada(self):
        return self.__sessao_encerrada
    
    @sessao_encerrada.setter
    def sessao_encerrada(self, valor):
        if type(valor) != "bool":
            raise ValueError("valor incorreto")
        self.__sessao_encerrada = valor

    def selecionar_sessao(self):
        if  not self.__sessao_encerrada:
            print(f"Data: {self.data_sessao}\n Horas: {self.hora_sessao}\nValor i: {self.valor_inteira}\nValor m: {self.valor_meia}")