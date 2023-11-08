from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app = Flask(__name__)
app.secret_key = "Mlsr5670101@#"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Mlsr5670101@#@localhost/aula_13_10"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

mysql = MySQL(app)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/setor', methods=['GET', 'POST'])
def setor():
    if request.method == 'POST':
        nome = request.form['nome']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO setor (nome) VALUES (%s)", (nome,))
        mysql.connection.commit()
        cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM setor")
    setores = cur.fetchall()
    cur.close()

    return render_template('setor.html', setores=setores)

@app.route('/funcionarios', methods=['GET', 'POST'])
def funcionarios():
    if request.method == 'POST':
        primeiro_nome = request.form['primeiro_nome']
        sobrenome = request.form['sobrenome']
        data_admissao = request.form['data_admissao']
        status_funcionario = request.form.get('status_funcionario')
        id_setor = request.form['id_setor']
        id_cargo = request.form['id_cargo']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO funcionarios (primeiro_nome, sobrenome, data_admissao, status_funcionario, id_setor, id_cargo) VALUES (%s, %s, %s, %s, %s, %s)", (primeiro_nome, sobrenome, data_admissao, status_funcionario, id_setor, id_cargo))
        mysql.connection.commit()
        cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM funcionarios")
    funcionarios = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM setor")
    setores = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cargos")
    cargos = cur.fetchall()
    cur.close()

    return render_template('funcionarios.html', funcionarios=funcionarios, setores=setores, cargos=cargos)

@app.route('/cargos', methods=['GET', 'POST'])
def cargos():
    if request.method == 'POST':
        nome = request.form['nome']
        id_setor = request.form['id_setor']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cargos (nome, id_setor) VALUES (%s, %s)", (nome, id_setor))
        mysql.connection.commit()
        cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cargos")
    cargos = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM setor")
    setores = cur.fetchall()
    cur.close()

    return render_template('cargos.html', cargos=cargos, setores=setores)

@app.route('/filtros')
def filtros():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM setor")
    setores = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM funcionarios")
    funcionarios = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cargos")
    cargos = cur.fetchall()
    cur.close()

    return render_template('filtros.html', setores=setores, funcionarios=funcionarios, cargos=cargos)

if __name__ == '__main__':
    app.run(debug=True)
