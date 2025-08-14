from app import app
from flask import render_template, request, redirect, url_for

from app.service.locadora_service import LocacaoService
from app.models.locacao_model import LocacaoModel
from app.service.filme_service import FilmeService
from app.models.filme_model import FilmeModel

locacao_service = LocacaoService()
filme_service = FilmeService()

@app.route('/')
def index():
    return redirect(url_for('listar_locacoes'))

@app.route('/locacoes')
def listar_locacoes():
    locacoes = locacao_service.get_all_locacoes()
    return render_template('locacoes/listar_locacoes.html', locacoes=locacoes)


@app.route('/locacoes/novo', methods=['GET', 'POST'])
def nova_locacao():
    if request.method == 'POST':
        data_locacao = request.form['data_locacao']
        data_devolucao = request.form['data_devolucao']
        cliente_nome = request.form['cliente_nome']
        id_filme = request.form['id_filme']
        
        locacao = LocacaoModel(None, data_locacao, data_devolucao, cliente_nome, id_filme)
        locacao_service.create_locacao(locacao)
        
        return redirect(url_for('listar_locacoes'))
    
    filmes = filme_service.get_all_filmes()
    return render_template('locacoes/nova_locacao.html', filmes=filmes)

@app.route('/locacoes/editar/<int:id>', methods=['GET', 'POST'])
def editar_locacao(id):
    locacao = locacao_service.get_locacao_by_id(id)
    if request.method == 'POST':
        locacao.set_data_locacao(request.form['data_locacao'])
        locacao.set_data_devolucao(request.form['data_devolucao'])
        locacao.set_cliente_nome(request.form['cliente_nome'])
        locacao.set_id_filme(request.form['id_filme'])
        
        locacao_service.update_locacao(locacao)
        
        return redirect(url_for('listar_locacoes'))
    
    filmes = filme_service.get_all_filmes()
    return render_template('locacoes/nova_locacao.html', locacao=locacao, filmes=filmes)

@app.route('/locacoes/excluir/<int:id>')
def excluir_locacao(id):
    locacao_service.delete_locacao(id)
    return redirect(url_for('listar_locacoes'))

@app.route('/filmes')
def listar_filmes():
    filmes = filme_service.get_all_filmes()
    return render_template('filmes/listar_filmes.html', filmes=filmes)

@app.route('/filmes/novo', methods=['GET', 'POST'])
def novo_filme():
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        ano_lancamento = request.form['ano_lancamento']
        
        
        filme = FilmeModel(None, titulo, genero, ano_lancamento)
        filme_service.add_filme(filme)
        
        return redirect(url_for('listar_filmes'))
    
    return render_template('filmes/novo_filme.html')

@app.route('/filmes/editar/<int:id>', methods=['GET', 'POST'])
def editar_filme(id):
    filme = filme_service.get_filme_by_id(id)
    if request.method == 'POST':
        filme.set_titulo(request.form['titulo'])
        filme.set_genero(request.form['genero'])
        filme.set_ano_lancamento(request.form['ano_lancamento'])
        
        filme_service.update_filme(filme)
        
        return redirect(url_for('listar_filmes'))
    
    return render_template('filmes/editar_filme.html', filme=filme)

@app.route('/filmes/excluir/<int:id>')
def excluir_filme(id):
    filme_service.delete_filme(id)
    return redirect(url_for('listar_filmes'))

