from app.database.connection import get_db
from app.models.filme_model import FilmeModel

class FilmeRepository:
    
    def get_all_filmes(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM filmes")
        rows = cursor.fetchall()
        return [FilmeModel(*row) for row in rows]
    
    def get_filme_by_id(self, id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM filmes WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return FilmeModel(*row)
        return None
    
    def add_filme(self, filme):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO filmes (titulo, genero, ano_lancamento) VALUES (?, ?, ?)",
                       (filme.get_titulo(), filme.get_genero(), filme.get_ano_lancamento()))
        db.commit()
        filme.set_id(cursor.lastrowid)
        return filme
    
    def update_filme(self, filme):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE filmes SET titulo = ?, genero = ?, ano_lancamento = ? WHERE id = ?",
                       (filme.get_titulo(), filme.get_genero(), filme.get_ano_lancamento(), filme.get_id()))
        db.commit()
        return filme
    
    def delete_filme(self, id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM filmes WHERE id = ?", (id,))
        db.commit()
        
    