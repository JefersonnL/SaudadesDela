from app import db  # Certifique-se de que 'app' é o nome do seu módulo Flask
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Banco de dados recriado com sucesso!")
