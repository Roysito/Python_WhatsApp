from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#Configuración de la base de datos SQLITE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRAK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Modelo de la tabla LOG
class log(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha_y_hora = db.Column(db.DateTime, default = datetime.utcnow)
    texto = db.Column(db.TEXT)
    
@app.route('/')
def hola_mundo():

    return render_template('holaflask.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)