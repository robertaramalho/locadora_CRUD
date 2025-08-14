from app.database.connection import get_db
from app.models.locacao_model import LocacaoModel

class LocacaoRepository:
    
    def get_all_locacoes(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""SELECT l.id, l.data_locacao, l.data_devolucao, l.cliente_nome, l.id_filme, f.titulo 
                          FROM locacao l 
                          JOIN filme f ON l.id_filme = f.id""")
        rows = cursor.fetchall()
        locacoes = []
        for row in rows:
            for row in rows:
                locacao = LocacaoModel(id=row[0],
                                       data_locacao=row[1],
                                       data_devolucao=row[2],
                                       cliente_nome=row[3],
                                       id_filme=row[4]
                                       )
            locacao.filme_titulo = row[5]
            locacoes.append(locacao)
        return locacoes
    
    def get_locacao_by_id(self, id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""SELECT l.id, l.data_locacao, l.data_devolucao, l.cliente_nome, l.id_filme, f.titulo 
                          FROM locacao l 
                          JOIN filme f ON l.id_filme = f.id 
                          WHERE l.id = ?""", (id,))
        row = cursor.fetchone()
        if row:
            locacao = LocacaoModel(id=row[0],
                                   data_locacao=row[1],
                                   data_devolucao=row[2],
                                   cliente_nome=row[3],
                                   id_filme=row[4]
                                   )
            locacao.filme_titulo = row[5]
            return locacao
        return None
    
    def add_locacao(self, locacao):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""INSERT INTO locacao (data_locacao, data_devolucao, cliente_nome, id_filme) 
                          VALUES (?, ?, ?, ?)""",
                       (locacao.get_data_locacao(), locacao.get_data_devolucao(), locacao.get_cliente_nome(), locacao.get_id_filme()))
        db.commit()
    
    def update_locacao(self, locacao):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""UPDATE locacao 
                          SET data_locacao = ?, data_devolucao = ?, cliente_nome = ?, id_filme = ? 
                          WHERE id = ?""",
                       (locacao.get_data_locacao(), locacao.get_data_devolucao(), locacao.get_cliente_nome(), locacao.get_id_filme(), locacao.get_id()))
        db.commit()
    
    def delete_locacao(self, id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM locacao WHERE id = ?", (id,))
        db.commit()
        
    def get_locacoes_by_filme_id(self, id_filme):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT f.titulo
            FROM locacao l
            JOIN filme f ON l.id_filme = f.id
            WHERE l.id_filme = ?
        """, (id_filme,))
        rows = cursor.fetchall()
        return [row[0] for row in rows] if rows else []
