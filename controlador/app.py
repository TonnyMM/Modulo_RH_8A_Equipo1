from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from modelo.DAO import db, Ciudades, Estados
app = Flask(__name__, template_folder='../vista', static_folder='../static')
Bootstrap(app)


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://userModRecursosHumanos:Hola.123@localhost/Mod_Recursos_Humanos'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'
@app.route('/')
def inicio():
    return render_template('comunes/login.html')

@app.route('/recopilarDatosLogin',methods=['post'])
def validarUsuario():
    return render_template('comunes/index.html')

@app.route('/estados')
def estados():
    e=Estados()
    estados = e.consultaGeneral()
    return render_template('estados/estadosListado.html',estados=estados)

@app.route('/estadosEdicion')
def estadosEdicion():
    return render_template('estados/estadosEditar.html')

@app.route('/estadosNuevo')
def estadosNuevo():
    return render_template('estados/estadosNuevo.html')


if __name__ == '__main__':
    app.run(debug=True)

