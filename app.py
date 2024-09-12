from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'  
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=30)  
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    @property
    def is_active(self):
        return True

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Nome de usuário já existe. Escolha um nome diferente.', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registro bem-sucedido! Você pode fazer login agora.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = 'remember' in request.form  # Verifica se a caixa de seleção está marcada
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user, remember=remember)  # Adiciona o parâmetro remember
            return redirect(url_for('welcome'))
        else:
            flash('Credenciais inválidas, tente novamente.', 'error')
    return render_template('login.html')

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado.', 'success')
    return redirect(url_for('login'))


@app.route('/treino_perna')
def treino_perna():
    return render_template('treino_perna.html')


@app.route('/treino_peito_triceps')
def treino_peito_triceps():
    return render_template('treino_peito_triceps.html')

# Rota para o treino de costas e bíceps
@app.route('/treino_costas_biceps')
def treino_costas_biceps():
    return render_template('treino_costas_biceps.html')

# Rota para o treino de ombros e abdômen
@app.route('/treino_ombros_abdomen')
def treino_ombros_abdomen():
    return render_template('treino_ombros_abdomen.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Garante que as tabelas sejam criadas
    app.run(debug=True)
