from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///asistentes.db'
db = SQLAlchemy(app)

class Asistente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nuevo_asistente = Asistente(
            tipo=request.form['tipo'],
            nombres=request.form['nombres'],
            apellidos=request.form['apellidos'],
            edad=int(request.form['edad']),
            correo=request.form['correo'],
            password=request.form['password']
        )
        db.session.add(nuevo_asistente)
        db.session.commit()
        return redirect(url_for('registro'))
    return render_template('formulario.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)

