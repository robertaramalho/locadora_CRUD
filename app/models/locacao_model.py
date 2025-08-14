class LocacaoModel:
    def __init__(self, id, data_locacao, data_devolucao, cliente_nome, id_filme):
        self.__id = id
        self.__data_locacao = data_locacao
        self.__data_devolucao = data_devolucao
        self.__cliente_nome = cliente_nome
        self.__id_filme = id_filme

    # Getters
    def get_id(self):
        return self.__id

    def get_data_locacao(self):
        return self.__data_locacao

    def get_data_devolucao(self):
        return self.__data_devolucao

    def get_cliente_nome(self):
        return self.__cliente_nome

    def get_id_filme(self):
        return self.__id_filme

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_data_locacao(self, data_locacao):
        self.__data_locacao = data_locacao

    def set_data_devolucao(self, data_devolucao):
        self.__data_devolucao = data_devolucao

    def set_cliente_nome(self, cliente_nome):
        self.__cliente_nome = cliente_nome

    def set_id_filme(self, id_filme):
        self.__id_filme = id_filme
