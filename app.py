from flask import Flask, redirect, render_template, url_for, request, flash
from Models import Tarefa  # Certifique-se de que o modelo Tarefa está definido corretamente
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'sua-chave-secreta-aqui'  # Adicione sua secret_key
db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        conteudo = request.form.get('tarefa')  # Corrigido
        if conteudo:  # Verifica se o conteúdo não é vazio
            nova_tarefa = Tarefa(conteudo=conteudo, status='pendente')
            db.session.add(nova_tarefa)
            db.session.commit()
            flash('Tarefa adicionada com sucesso!', 'success')
        else:
            flash('Conteúdo da tarefa não pode ser vazio', 'danger')
    
    # Exibir todas as tarefas
    all_user = Tarefa.query.all()
    return render_template('home.html', all_user=all_user)

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    tarefa_eliminar = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa_eliminar)
    db.session.commit()
    flash('Tarefa eliminada com sucesso!', 'success')  # Mensagem de sucesso
    return redirect(url_for('home'))

@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    nova_descricao = request.form.get('editar')  # Corrigido
    tarefa = Tarefa.query.get_or_404(id)
    if nova_descricao:
        tarefa.conteudo = nova_descricao
        db.session.commit()
        flash('Tarefa editada com sucesso!', 'success')  # Mensagem de sucesso
    else:
        flash('Descrição da tarefa não pode ser vazia', 'danger')
    return redirect(url_for('home'))

@app.route('/concluir/<int:id>', methods=['POST'])
def concluir(id):
    tarefa = Tarefa.query.get_or_404(id)
    tarefa.status = 'concluido'
    db.session.commit()
    flash('Tarefa concluída com sucesso!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)




































if __name__=='__main__':
    with app.app_context():
        app.run(debug=True)