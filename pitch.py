from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Banco de dados SQLite
def criar_tabela():
    conn = sqlite3.connect('pitch.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pitches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            curso TEXT,
            objetivo TEXT,
            tecnologia TEXT,
            habilidade1 TEXT,
            habilidade2 TEXT,
            empresa TEXT,
            diferencial TEXT,
            experiencia TEXT,
            softskill TEXT,
            conquista TEXT,
            projeto_desejado TEXT,
            formato TEXT,
            disponibilidade TEXT
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()
  
@app.route('/', methods=['GET', 'POST'])
def index():
    pitch_texto = ''
    
    if request.method == 'POST':
        try:
            dados = request.form
            print("📥 Dados recebidos:", dados)

            conn = sqlite3.connect('pitch.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO pitches (
                    nome, curso, objetivo, tecnologia, habilidade1, habilidade2,
                    empresa, diferencial, experiencia, softskill, conquista,
                    projeto_desejado, formato, disponibilidade
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                dados.get('nome'), dados.get('curso'), dados.get('objetivo'),
                dados.get('tecnologia'), dados.get('habilidade1'), dados.get('habilidade2'),
                dados.get('empresa'), dados.get('diferencial'), dados.get('experiencia'),
                dados.get('softskill'), dados.get('conquista'), dados.get('projeto_desejado'),
                dados.get('formato'), dados.get('disponibilidade')
            ))
            conn.commit()
            conn.close()

            # Geração do pitch
            pitch_texto = f"""
            <div class='success'>
                <h2>🎤 Seu Pitch Profissional</h2>
                <p>Olá! Meu nome é <strong>{dados.get('nome')}</strong>, sou da área de <strong>{dados.get('curso')}</strong> e tenho como objetivo atuar em <strong>{dados.get('objetivo')}</strong>.</p>
                <p>Tenho experiência com <strong>{dados.get('tecnologia')}</strong> e minhas principais habilidades são <strong>{dados.get('habilidade1')}</strong> e <strong>{dados.get('habilidade2')}</strong>.</p>
                <p>Um diferencial que me destaca é <strong>{dados.get('diferencial')}</strong>. Já participei de <strong>{dados.get('experiencia')}</strong>, onde desenvolvi minha <strong>{dados.get('softskill')}</strong>.</p>
                <p>Uma conquista que me orgulho é <strong>{dados.get('conquista')}</strong>. Tenho como meta trabalhar na <strong>{dados.get('empresa')}</strong>, especialmente em <strong>{dados.get('projeto_desejado')}</strong>.</p>
                <p>Estou disponível para atuar em formato <strong>{dados.get('formato')}</strong>, com disponibilidade <strong>{dados.get('disponibilidade')}</strong>.</p>
            </div>
            """

        except Exception as e:
            pitch_texto = f"<div class='success'><p style='color:red'>❌ Erro ao salvar pitch: {e}</p></div>"
            print("⚠️ Erro:", e)

    return render_template_string(HTML_TEMPLATE + pitch_texto)



HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Pro Pitch Generator</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(120deg, #1a032a, #32004e);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px;
            color: white;
        }

        .container {
            background: rgba(255, 255, 255, 0.06);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            padding: 40px;
            width: 100%;
            max-width: 800px;
            box-shadow: 0 0 20px rgba(128, 0, 255, 0.3);
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
            color: #c084fc;
            font-size: 28px;
        }

        form {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        form label {
            font-size: 14px;
            margin-bottom: 6px;
            display: block;
        }

        form input,
        form textarea {
            width: 100%;
            padding: 10px;
            border-radius: 10px;
            border: none;
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
            font-size: 14px;
            outline: none;
            transition: background 0.3s ease;
        }

        form input:focus,
        form textarea:focus {
            background: rgba(255, 255, 255, 0.2);
        }

        textarea {
            grid-column: span 2;
            resize: none;
        }

        button {
            grid-column: span 2;
            padding: 15px;
            border: none;
            border-radius: 12px;
            background: linear-gradient(to right, #8b5cf6, #a855f7);
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        button:hover {
            background: linear-gradient(to right, #9333ea, #7c3aed);
        }

        .success {
            margin-top: 30px;
            text-align: center;
            font-size: 18px;
            color: #b794f4;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Pro Pitch Generator</h1>
        <form method="POST">
            <div>
                <label>Seu nome:</label>
                <input name="nome" required>
            </div>
            <div>
                <label>Curso ou área:</label>
                <input name="curso" required>
            </div>
            <div>
                <label>Objetivo profissional:</label>
                <input name="objetivo" required>
            </div>
            <div>
                <label>Tecnologia preferida:</label>
                <input name="tecnologia" required>
            </div>
            <div>
                <label>Habilidade 1:</label>
                <input name="habilidade1" required>
            </div>
            <div>
                <label>Habilidade 2:</label>
                <input name="habilidade2" required>
            </div>
            <div>
                <label>Empresa dos sonhos:</label>
                <input name="empresa" required>
            </div>
            <div>
                <label>Diferencial:</label>
                <input name="diferencial" required>
            </div>
            <div>
                <label>Experiência ou projeto:</label>
                <input name="experiencia" required>
            </div>
            <div>
                <label>Soft Skill:</label>
                <input name="softskill" required>
            </div>
            <div>
                <label>Conquista:</label>
                <input name="conquista" required>
            </div>
            <div>
                <label>Projeto desejado:</label>
                <input name="projeto_desejado" required>
            </div>
            <div>
                <label>Formato de trabalho:</label>
                <input name="formato" required>
            </div>
            <div>
                <label>Disponibilidade:</label>
                <input name="disponibilidade" required>
            </div>
            <button type="submit">Gerar Pitch</button>
        </form>
    </div>
</body>
</html>
"""


if __name__ == '__main__':
    app.run(debug=True)
