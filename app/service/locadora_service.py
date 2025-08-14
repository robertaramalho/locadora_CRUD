from app.models.locacao_model import LocacaoModel
from app.repository.locacao_repository import LocacaoRepository
from app.service.filme_service import FilmeService
from datetime import datetime

class LocacaoService:
    def __init__(self):
        self.locacao_repository = LocacaoRepository()
        self.filme_service = FilmeService()

    def get_all_locacoes(self):
        return self.locacao_repository.get_all_locacoes()

    def get_locacao_by_id(self, id):
        return self.locacao_repository.get_locacao_by_id(id)

    def create_locacao(self, locacao: LocacaoModel):
        self._validar_datas(locacao)
        self._validar_filme_disponivel(locacao)
        self.locacao_repository.add_locacao(locacao)

    def update_locacao(self, locacao: LocacaoModel):
        self._validar_datas(locacao)
        self._validar_filme_disponivel(locacao, ignorar_id=locacao.get_id())
        self.locacao_repository.update_locacao(locacao)

    def delete_locacao(self, id):
        self.locacao_repository.delete_locacao(id)

    def _validar_datas(self, locacao: LocacaoModel):
        """
        Valida datas de locação e devolução.
        """
        try:
            data_locacao = datetime.strptime(locacao.get_data_locacao(), "%Y-%m-%d")
            data_devolucao = datetime.strptime(locacao.get_data_devolucao(), "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de data inválido. Use o padrão YYYY-MM-DD.")

        if data_locacao > data_devolucao:
            raise ValueError("A data de locação não pode ser maior que a data de devolução.")

        if data_locacao.date() > datetime.today().date():
            raise ValueError("A data de locação não pode estar no futuro.")

    def _validar_filme_disponivel(self, locacao: LocacaoModel, ignorar_id=None):
        """
        Verifica se o filme já está locado e não foi devolvido.
        """
        todas_locacoes = self.locacao_repository.get_all_locacoes()
        hoje = datetime.today().date()

        for l in todas_locacoes:
            if ignorar_id is not None and l.get_id() == ignorar_id:
                continue  

            data_devolucao = datetime.strptime(l.get_data_devolucao(), "%Y-%m-%d").date()

            if int(l.get_id_filme()) == int(locacao.get_id_filme()) and data_devolucao >= hoje:

                filme = self.filme_service.get_filme_by_id(l.get_id_filme())
                nome_filme = filme.get_titulo() if filme else f"ID {l.get_id_filme()}"
                raise ValueError(
                    f"O filme '{nome_filme}' já está locado até {data_devolucao.strftime('%d/%m/%Y')}."
                )