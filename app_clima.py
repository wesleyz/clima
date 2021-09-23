from flask import Flask, render_template, url_for
app = Flask(__name__)
import clima
from waitress import serve


cli = clima.clima()
cli.recupera_condicoes_meteorologicas()
cli.atualiza_banco()

valores = cli.load_data_from_database()


posts = [
    {
        'author': 'Wesley Pereira',
        'title': 'Atualizado direto no código',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Fulano de Tal',
        'title': 'Postagem 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }, 
    {
        'author': 'Beltrano de Tal',
        'title': 'Postagem 3',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }, 
    {
        'author': 'Cicrano de Tal',
        'title': 'Postagem 4',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('registro.html', title='Registro', dados=valores.values)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/login")
def login():
    return render_template('login.html', title='Login')


@app.route("/admin")
def admin():
    return render_template('login.html', title='Admin')

@app.route("/register")
def register():
    return render_template('registro.html', title='Registro', dados=valores.values)
    


if __name__ == '__main__':
    #app.run(debug=True, port=5001)
    serve(app, host='0.0.0.0', port=8080) 
