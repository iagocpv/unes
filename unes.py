from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", title="Home", bg="class=bg-1")

@app.route('/quemsomos')
def quem_somos():
    return render_template("quem somos.html", title="Quem Somos", bg="class=bg-2")

@app.route('/contato')
def contato():
    return render_template("contato.html", title="Contato", bg="class=bg-2")
