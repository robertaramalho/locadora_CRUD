class FilmeModel:
    def __init__(self, id, titulo, genero, ano_lancamento):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__ano_lancamento = ano_lancamento

    # Getters
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def get_ano_lancamento(self):
        return self.__ano_lancamento

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero

    def set_ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento
