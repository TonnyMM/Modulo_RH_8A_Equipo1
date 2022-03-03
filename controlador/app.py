from flask import Flask,render_template,request,flash,redirect,url_for
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

#######################################################################################################################
@app.route('/estados')
def estados():
    e = Estados()
    estados = e.consultaGeneral()
    return render_template('estados/estadosListado.html',estados = estados)

@app.route('/estadosNuevo')
def estadosNuevo():
    return render_template('estados/estadosNuevo.html')

@app.route('/registrarEstado',methods=['post'])
def registrarEstado():
    e = Estados()
    e.nombre = request.form['nombre']
    e.siglas= request.form['siglas']
    e.insertar()
    flash('Se ha registrado un nuevo estado con éxito!!')
    return render_template('estados/estadosNuevo.html')

@app.route('/estadosEditar/<int:id>')
def estadosEditar(id):
    e = Estados()
    return render_template('estados/estadosEditar.html', estado = e.consultaIndividual(id))

@app.route('/guardarEstado',methods=['post'])
def guardarEstado():
    e = Estados()
    e.idEstado = request.form['idEstado']
    e.nombre = request.form['nombre']
    e.siglas = request.form['siglas']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        e.estatus=True
    else:
        e.estatus=False
    e.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('estados/estadosEditar.html', estado = e.consultaIndividual(request.form['idEstado']))

@app.route('/estadosEliminar/<int:id>')
def estadosEliminar(id):
    e = Estados()
    e.eliminar(id)
    flash('Se ha eliminado el estado con éxito!!')
    return redirect(url_for('estados'))

#######################################################################################################################
@app.route('/ciudades')
def ciudades():
    c = Ciudades()
    ciudades = c.consultaGeneral()
    e = Estados ()
    estados = e.consultaGeneral()
    return render_template('ciudades/ciudadesListado.html',ciudades = ciudades, estados = estados)

@app.route('/ciudadesNuevo')
def ciudadesNuevo():
    e = Estados()
    estados = e.consultaGeneral()
    return render_template('ciudades/ciudadesNuevo.html',estados=estados)

@app.route('/registrarCiudad',methods=['post'])
def registrarCiudad():
    c = Ciudades()
    c.nombre = request.form['nombre']
    c.idEstado= request.form['idEstado']
    c.insertar()
    flash('Se ha registrado un nueva ciudad con éxito!!')
    return render_template('ciudades/ciudadesNuevo.html')

@app.route('/ciudadesEditar/<int:id>')
def ciudadesEditar(id):
    c = Ciudades()
    e = Estados()
    return render_template('ciudades/ciudadesEditar.html', ciudad = c.consultaIndividual(id),estados = e.consultaGeneral())

@app.route('/guardarCiudad',methods=['post'])
def guardarCiudad():
    c = Ciudades()
    c.idCiudad = request.form['idCiudad']
    c.nombre = request.form['nombre']
    c.idEstado = request.form['idEstado']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        c.estatus=True
    else:
        c.estatus=False
    c.actualizar()
    e = Estados()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('ciudades/ciudadesEditar.html', ciudad = c.consultaIndividual(request.form['idCiudad']),estados=e.consultaGeneral())

@app.route('/ciudadesEliminar/<int:id>')
def ciudadesEliminar(id):
    c = Ciudades()
    c.eliminar(id)
    flash('Se ha eliminado la ciudad con éxito!!')
    return redirect(url_for('ciudades'))


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

