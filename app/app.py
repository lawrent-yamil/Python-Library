from flask import Flask, render_template, request, redirect, session
from connectSQL import get_books, search_user, add_user

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secreto'
    
    @app.route('/')
    def index():
        if 'username' in session:
            return render_template('index.html', books=get_books())
        return render_template('index.html', books=get_books())

    @app.route('/revistas')
    def revistas():
        return render_template('revistas.html')

    @app.route('/enciclopedia')
    def enciclopedia():
        return render_template('enciclopedia.html')

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        return render_template('login.html')
    
    @app.route('/logout')
    def logout():
        session.pop('username', None)
        return redirect('/')

    @app.route('/signup', methods=['POST', 'GET'])
    def signup():
        return render_template('signup.html')

    @app.route('/provar_data', methods=['POST'])
    def provar_data():
        if request.method == 'POST':
            usuario = request.form['usuario']
            cedula = request.form['cedula']
            if search_user(cedula, usuario):
                session['username'] = usuario
                return redirect('/')
            else:
                return redirect('/login')
    
    @app.route('/provar_signup', methods=['POST'])
    def provar_signup():
        if request.method == 'POST':
            usuario = request.form['usuario']
            cedula = request.form['cedula']
            add_user(usuario, cedula)
            session['username'] = usuario
            return redirect('/')
    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)