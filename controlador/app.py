from flask import Flask,render_template,request,flash,redirect,url_for
from flask_bootstrap import Bootstrap
from modelo.DAO import db, Ciudades, Estados, Departamentos, Puestos, Turnos

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

#######################################################################################################################
@app.route('/departamentos')
def departamentos():
    d = Departamentos()
    departamentos = d.consultaGeneral()
    return render_template('departamentos/departamentosListado.html',departamentos = departamentos)

@app.route('/departamentosNuevo')
def departamentosNuevo():
    activado = 1
    return render_template('departamentos/departamentosNuevo.html',activado=activado)

@app.route('/registrarDepartamento',methods=['post'])
def registrarDepartamento():
    d = Departamentos()
    d.nombre = request.form['nombre']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        d.estatus=True
    else:
        d.estatus=False
    d.insertar()
    activado = 1
    flash('Se ha registrado un nuevo departamento con éxito!!')
    return render_template('departamento/departamentosNuevo.html', activado=activado)

@app.route('/departamentosEditar/<int:id>')
def departamentosEditar(id):
    d = Departamentos()
    return render_template('departamentos/departamentosEditar.html', departamento = d.consultaIndividual(id))

@app.route('/guardarDepartamento',methods=['post'])
def guardarDepartamento():
    d = Departamentos()
    d.idDepartamento = request.form['idDepartamento']
    d.nombre = request.form['nombre']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        d.estatus=True
    else:
        d.estatus=False
    d.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('departamentos/departamentosEditar.html', departamento = d.consultaIndividual(request.form['idDepartamento']))

@app.route('/departamentosEliminar/<int:id>')
def departamentosEliminar(id):
    d = Departamentos()
    d.eliminar(id)
    flash('Se ha eliminado el departamento con éxito!!')
    return redirect(url_for('departamentos'))

#######################################################################################################################
@app.route('/puestos')
def puestos():
    p = Puestos()
    puestos = p.consultaGeneral()
    return render_template('puestos/puestosListado.html',puestos = puestos)

@app.route('/puestosNuevo')
def puestosNuevo():
    activado = 1
    return render_template('puestos/puestosNuevo.html',activado=activado)

@app.route('/registrarPuesto',methods=['post'])
def registrarPuesto():
    p = Puestos()
    p.nombre = request.form['nombre']
    p.salarioMinimo = request.form['salarioMinimo']
    p.salarioMaximo = request.form['salarioMaximo']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        p.estatus=True
    else:
        p.estatus=False
    p.insertar()
    activado = 1
    flash('Se ha registrado un nuevo puesto con éxito!!')
    return render_template('puestos/puestosNuevo.html', activado=activado)

@app.route('/puestosEditar/<int:id>')
def puestosEditar(id):
    p = Puestos()
    return render_template('puestos/puestosEditar.html', puesto = p.consultaIndividual(id))

@app.route('/guardarPuesto',methods=['post'])
def guardarPuesto():
    p = Puestos()
    p.idPuesto = request.form['idPuesto']
    p.nombre = request.form['nombre']
    p.salarioMinimo = request.form['salarioMinimo']
    p.salarioMaximo = request.form['salarioMaximo']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        p.estatus=True
    else:
        p.estatus=False
    p.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('puestos/puestosEditar.html', puesto = p.consultaIndividual(request.form['idPuesto']))

@app.route('/puestosEliminar/<int:id>')
def puestosEliminar(id):
    p = Puestos()
    p.eliminar(id)
    flash('Se ha eliminado el puesto con éxito!!')
    return redirect(url_for('puestos'))

#######################################################################################################################
@app.route('/turnos')
def turnos():
    t = Turnos()
    turnos = t.consultaGeneral()
    return render_template('turnos/turnosListado.html',turnos = turnos)

@app.route('/turnosNuevo')
def turnosNuevo():
    return render_template('turnos/turnosNuevo.html')

@app.route('/registrarTurno',methods=['post'])
def registrarTurno():
    t = Turnos()
    t.nombre = request.form['nombre']
    t.horaInicio = request.form['horaInicio']
    t.horaFin = request.form['horaFin']
    t.dias = request.form['dias']
    t.insertar()
    flash('Se ha registrado un nuevo turno con éxito!!')
    return render_template('turnos/turnosNuevo.html')

@app.route('/turnosEditar/<int:id>')
def turnosEditar(id):
    t = Turnos()
    return render_template('turnos/turnosEditar.html', turno = t.consultaIndividual(id))

@app.route('/guardarTurno',methods=['post'])
def guardarTurno():
    t = Turnos()
    t.idTurno = request.form['idTurno']
    t.nombre = request.form['nombre']
    t.horaInicio = request.form['horaInicio']
    t.horaFin = request.form['horaFin']
    t.dias = request.form['horaFin']
    t.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('turnos/turnosEditar.html', turno = t.consultaIndividual(request.form['idTurno']))

@app.route('/turnosEliminar/<int:id>')
def turnosEliminar(id):
    t = Turnos()
    t.eliminar(id)
    flash('Se ha eliminado el turno con éxito!!')
    return redirect(url_for('turnos'))

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

