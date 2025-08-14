from app.models.filme_model import FilmeModel
from app.repository.filme_repository import FilmeRepository
from app.repository.locacao_repository import LocacaoRepository
import datetime

class FilmeService:
    def __init__(self):
        self.filme_repository = FilmeRepository()
        self.locacao_repository = LocacaoRepository()

    def get_all_filmes(self):
        return self.filme_repository.get_all_filmes()

    def get_filme_by_id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("O ID do filme deve ser um número inteiro positivo.")
        filme = self.filme_repository.get_filme_by_id(id)
        if not filme:
            raise ValueError("Filme não encontrado.")
        return filme

    def add_filme(self, filme: FilmeModel):
        self.__validar_filme(filme)
        self.filme_repository.add_filme(filme)

    def update_filme(self, filme: FilmeModel):
        if not filme.get_id():
            raise ValueError("O filme deve ter um ID válido para ser atualizado.")
        self.__validar_filme(filme)
        self.filme_repository.update_filme(filme)

    def delete_filme(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("O ID do filme deve ser um número inteiro positivo.")
        
        locacoes = self.locacao_repository.get_locacoes_by_filme_id(id)
        if locacoes:
            raise ValueError(
                f"Não é possível excluir o filme '{locacoes[0]}' pois existem locações vinculadas a ele."
            )

        
        self.filme_repository.delete_filme(id)

    def __validar_filme(self, filme: FilmeModel):
        if not filme.get_titulo() or not filme.get_titulo().strip():
            raise ValueError("O título do filme é obrigatório.")
        if len(filme.get_titulo()) < 3:
            raise ValueError("O título do filme não pode ter menos de 3 caracteres.")


        if not filme.get_genero() or not filme.get_genero().strip():
            raise ValueError("O gênero do filme é obrigatório.")
        if len(filme.get_genero()) < 3:
            raise ValueError("O gênero do filme não pode ter menos de 3 caracteres.")

        ano = filme.get_ano_lancamento()
        ano_atual = datetime.datetime.now().year
        if not str(ano).isdigit() or int(ano) < 1888 or int(ano) > ano_atual:
            raise ValueError(f"O ano de lançamento deve ser entre 1888 e {ano_atual}.")
