class Application:
    def __init__(self):
        self.asssento = []
        self.ator = []
        self.atua = []
        self.filme = []
        self.genero = []
        self.ingresso = []
        self.sala = []
        self.sessao = []
        self.op_menu = {}

    def menu(self, op):
        print("""
        1 - Cadastrar assento
        2 - Cadastrar ator
        3 - Cadastrar atua
        4 - Cadastrar filme
        5 - Cadastrar genero
        6 - Cadastrar ingresso
        7 - Cadastrar sala
        8 - Cadastrar sessões
        """)
        

app = Application()
app.menu(3)