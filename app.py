from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "admin"
mysql = MySQL(app)

with app.app_context():
    con = mysql.connect
    cursor = con.cursor()
    cursor.execute('''
            CREATE DATABASE IF NOT EXISTS unes;
            USE unes;
            CREATE TABLE IF NOT EXISTS contatos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(40),
                assunto VARCHAR(20),
                descricao VARCHAR(50)
            );
    ''')
    cursor.close()

app.config["MYSQL_DB"] = "unes"


@app.route('/')
def home():
    return render_template("home.html", title="Home", bg="class=bg-1")

@app.route('/quemsomos')
def quem_somos():
    return render_template("quem somos.html", title="Quem Somos", bg="class=bg-2")

@app.route('/contato', methods=["GET", "POST"] )
def contato():
    if request.method == "POST":
        email = request.form["email"]
        assunto = request.form["assunto"]
        descricao = request.form["descricao"]
        con = mysql.connection
        cur = con.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao)VALUES(%s, %s, %s)", (email, assunto, descricao))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('contato'))
    return render_template("contato.html", title="Contato", bg="class=bg-2")

@app.route('/users')
def users():
    con = mysql.connection
    cur = con.cursor()
    users = cur.execute("SELECT * FROM contatos")
    userDetails = []
    if users > 0:
        userDetails = cur.fetchall()
    cur.close()
    print(userDetails)
    return render_template("users.html", title="Usuários", bg="class=bg-2", userDetails=userDetails)

if __name__ == "__main__":
    app.run(debug=True)