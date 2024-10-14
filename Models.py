from datetime import datetime
from db import db

class Tarefa(db.Model):
    __tablename__ = 'tarefas'
    id = db.Column(db.Integer, primary_key = True)
    conteudo = db.Column(db.String(200))
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String, default='pendente') 
    

    def __repr__(self):
        return f"<Tarefa(id={self.id}, conteudo='{self.conteudo}', status='{self.status}')>"

 
 