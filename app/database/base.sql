CREATE TABLE filme (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    genero TEXT NOT NULL,
    ano_lancamento INTEGER NOT NULL
);

CREATE TABLE locacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_locacao DATE NOT NULL,
    data_devolucao DATE,
    cliente_nome TEXT NOT NULL,
    id_filme INTEGER NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES filme(id)
);
