from app.models.locacao_model import LocacaoModel
from app.repository.locacao_repository import LocacaoRepository

class LocacaoService:
    def __init__(self):
        self.locacao_repository = LocacaoRepository()

    def get_all_locacoes(self):
        return self.locacao_repository.get_all_locacoes()

    def get_locacao_by_id(self, id):
        return self.locacao_repository.get_locacao_by_id(id)

    def create_locacao(self, locacao: LocacaoModel):
        self.locacao_repository.add_locacao(locacao)

    def update_locacao(self, locacao: LocacaoModel):
        self.locacao_repository.update_locacao(locacao)

    def delete_locacao(self, id):
        self.locacao_repository.delete_locacao(id)
