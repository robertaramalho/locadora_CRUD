# 🎬 Sistema de Locadora de Filmes da Robertinha

Este projeto é um sistema simples para gerenciar **filmes** e **locações** de uma locadora.

## 📂 Entidades

### 1. Filme
Representa os filmes cadastrados no sistema.

**Atributos:**
- `id` *(INTEGER)* — Identificador único do filme.
- `titulo` *(TEXT)* — Nome do filme.
- `genero` *(TEXT)* — Gênero do filme (ex.: Ação, Drama, Comédia).
- `ano_lancamento` *(INTEGER)* — Ano de lançamento do filme.

### 2. Locação
Representa o registro de um cliente que alugou um filme.

**Atributos:**
- `id` *(INTEGER)* — Identificador único da locação.
- `data_locacao` *(DATE)* — Data em que o filme foi alugado.
- `data_devolucao` *(DATE)* — Data em que o filme foi devolvido (pode ser nula se ainda não devolvido).
- `cliente_nome` *(TEXT)* — Nome do cliente que alugou o filme.
- `id_filme` *(INTEGER)* — ID do filme alugado (chave estrangeira para `filme.id`).

## 🔗 Relacionamento
- Relacionamento **1:N** (*Um filme pode ter várias locações*).
- Uma locação sempre está associada a **um único filme**.

- **Não é possível excluir um filme** que já possua locações registradas.

### Como Executar o projeto:

1. Criar ambiente virtual
    ```
    python -m venv venv
    ```
2. Ativar ambiente virtual
    ```
    venv/Scripts/activate
    ```
   2.1. Atualizar o pip
   ```
    pip install --upgrade pip
    ```
3. Instalar o Flask
    ```
    pip install Flask
    ```
4. Executar o script `run.py`
```
python run.py
```

