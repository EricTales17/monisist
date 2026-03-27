from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('escolar.db')
    cursor = conn.cursor()
    # Tabela adaptada para Alunos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            turma TEXT NOT NULL,
            status TEXT DEFAULT 'Presente',
            tempo_saida TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Rota para a tela de LOGIN e DASHBOARD (Seu primeiro código)
@app.route('/')
def index():
    return render_template('login.html')

# Rota para a tela de CADASTRO (Seu segundo código)
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        turma = request.form['turma'] # Adaptado de 'email' para 'turma'
        
        conn = sqlite3.connect('escolar.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO alunos (nome, turma) VALUES (?, ?)', (nome, turma))
        conn.commit()
        conn.close()
        return redirect(url_for('cadastro'))

    conn = sqlite3.connect('escolar.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()
    conn.close()
    return render_template('cadastro.html', alunos=alunos)

# Rota API para o JavaScript do Dashboard buscar os alunos
@app.route('/api/alunos')
def api_alunos():
    conn = sqlite3.connect('escolar.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome, status, tempo_saida FROM alunos')
    alunos = [{"nome": a[0], "status": a[1], "tempo": a[2]} for a in cursor.fetchall()]
    conn.close()
    return jsonify(alunos)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)