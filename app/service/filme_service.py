from app.models.filme_model import FilmeModel
from app.repository.filme_repository import FilmeRepository
from app.repository.locacao_repository import LocacaoRepository

class FilmeService:
    def __init__(self):
        self.filme_repository = FilmeRepository()
        self.locacao_repository = LocacaoRepository()

    def get_all_filmes(self):
        return self.filme_repository.get_all_filmes()

    def get_filme_by_id(self, id):
        return self.filme_repository.get_filme_by_id(id)

    def add_filme(self, filme: FilmeModel):
        self.filme_repository.add_filme(filme)

    def update_filme(self, filme: FilmeModel):
        self.filme_repository.update_filme(filme)

    def delete_filme(self, id):
        # Validação: Não pode deletar se houver locação vinculada
        locacoes = self.locacao_repository.get_locacoes_by_filme_id(id)
        if locacoes:
            raise Exception("Não é possível excluir o filme pois existem locações vinculadas a ele.")
        self.filme_repository.delete_filme(id)
