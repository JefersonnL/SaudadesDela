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

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  
    comment = db.Column(db.Text, nullable=True)  

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
        remember = 'remember' in request.form  
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user, remember=remember)  
            return redirect(url_for('profile'))  
        else:
            flash('Credenciais inválidas, tente novamente.', 'error')
    
    comments = Comment.query.all()  
    reviews = Review.query.all()  
    return render_template('login.html', comments=comments, reviews=reviews)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Atualiza o usuário no banco de dados
        current_user.username = username
        if password: 
            current_user.password = generate_password_hash(password, method='pbkdf2:sha256')
        db.session.commit()

        flash('Perfil atualizado com sucesso!', 'success')
        return redirect(url_for('profile'))

    return render_template('edit_profile.html')

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

# Rota para o treino de pernas
@app.route('/treino_perna')
def treino_perna():
    return render_template('treino_perna.html')

# Rota para o treino de peito
@app.route('/treino_peito')
def treino_peito():
    return render_template('treino_peito.html')

# Rota para o treino de tríceps
@app.route('/treino_triceps')
def treino_triceps():
    return render_template('treino_triceps.html')

# Rota para o treino de costas
@app.route('/treino_costas')
def treino_costas():
    return render_template('treino_costas.html')

# Rota para o treino de bíceps
@app.route('/treino_biceps')
def treino_biceps():
    return render_template('treino_biceps.html')

# Rota para o treino de ombros
@app.route('/treino_ombros')
def treino_ombros():
    return render_template('treino_ombros.html')

# Rota para o treino de abdômen
@app.route('/treino_abdomen')
def treino_abdomen():
    return render_template('treino_abdomen.html')

@app.route('/comment', methods=['POST'])
def comment():
    if request.method == 'POST':
        username = request.form['username']
        content = request.form['content']
        
        new_comment = Comment(username=username, content=content)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comentário adicionado com sucesso!', 'success')
        
    return redirect(url_for('login'))

@app.route('/review', methods=['POST'])
def review():
    if request.method == 'POST':
        username = request.form['username']
        rating = request.form['rating']
        comment = request.form.get('comment', '')  
        
        new_review = Review(username=username, rating=rating, comment=comment)
        db.session.add(new_review)
        db.session.commit()
        flash('Avaliação adicionada com sucesso!', 'success')
        
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Garante que as tabelas sejam criadas
    app.run(debug=True)
