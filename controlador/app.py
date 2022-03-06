from flask import Flask,render_template,request,flash,redirect,url_for
from flask_bootstrap import Bootstrap
from modelo.DAO import db, Ciudades, Estados, Departamentos, Puestos, Turnos, Percepciones, Deducciones, Periodos, FormasPago

app = Flask(__name__, template_folder='../vista', static_folder='../static')
Bootstrap(app)
import json

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

@app.route('/estado/nombre/<string:nombre>',methods=['get'])
def consultarEstado(nombre):
    estado=Estados()
    return json.dumps(estado.consultarEstados(nombre))

@app.route('/estadoSig/siglas/<string:siglas>',methods=['get'])
def consultarEstadoSig(siglas):
    estadoSig=Estados()
    return json.dumps(estadoSig.consultarEstSig(siglas))

@app.route('/ciudad/nombre/<string:nombre>',methods=['get'])
def consultarCiudad(nombre):
    ciudad=Ciudades()
    return json.dumps(ciudad.consultarCiudades(nombre))

@app.route('/departamento/nombre/<string:nombre>',methods=['get'])
def consultarDepartamento(nombre):
    departamento=Departamentos()
    return json.dumps(departamento.consultarDepartamentos(nombre))

@app.route('/puesto/nombre/<string:nombre>',methods=['get'])
def consultarPuestos(nombre):
    puesto=Puestos()
    return json.dumps(puesto.consultarPuestos(nombre))

@app.route('/turno/nombre/<string:nombre>',methods=['get'])
def consultarTurno(nombre):
    turno=Turnos()
    return json.dumps(turno.consultarTurnos(nombre))

@app.route('/percepcion/nombre/<string:nombre>',methods=['get'])
def consultarPercepcion(nombre):
    percepcion=Percepciones()
    return json.dumps(percepcion.consultarPercepciones(nombre))

@app.route('/deduccion/nombre/<string:nombre>',methods=['get'])
def consultarDeduccion(nombre):
    deduccion=Deducciones()
    return json.dumps(deduccion.consultarDeducciones(nombre))

@app.route('/periodo/nombre/<string:nombre>',methods=['get'])
def consultarPeriodo(nombre):
    periodo=Periodos()
    return json.dumps(periodo.consultarPeriodos(nombre))

@app.route('/formaPago/nombre/<string:nombre>',methods=['get'])
def consultarFormaPago(nombre):
    formaPago=FormasPago()
    return json.dumps(formaPago.consultarFormasPago(nombre))

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
    return render_template('departamentos/departamentosNuevo.html', activado=activado)

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

#######################################################################################################################
@app.route('/percepciones')
def percepciones():
    p = Percepciones()
    percepciones = p.consultaGeneral()
    return render_template('percepciones/percepcionesListado.html',percepciones = percepciones)

@app.route('/percepcionesNuevo')
def percepcionesNuevo():
    return render_template('percepciones/percepcionesNuevo.html')

@app.route('/registrarPercepcion',methods=['post'])
def registrarPercepcion():
    p = Percepciones()
    p.nombre = request.form['nombre']
    p.descripcion = request.form['descripcion']
    p.diasPagar = request.form['diasPagar']
    p.insertar()
    flash('Se ha registrado un nueva percepcion con éxito!!')
    return render_template('percepciones/percepcionesNuevo.html')

@app.route('/percepcionesEditar/<int:id>')
def percepcionesEditar(id):
    p = Percepciones()
    return render_template('percepciones/percepcionesEditar.html', percepcion = p.consultaIndividual(id))

@app.route('/guardarPercepcion',methods=['post'])
def guardarPercepcion():
    p = Percepciones()
    p.idPercepcion = request.form['idPercepcion']
    p.nombre = request.form['nombre']
    p.descripcion = request.form['descripcion']
    p.diasPagar = request.form['diasPagar']
    p.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('percepciones/percepcionesEditar.html', percepcion = p.consultaIndividual(request.form['idPercepcion']))

@app.route('/percepcionesEliminar/<int:id>')
def percepcionesEliminar(id):
    p = Percepciones()
    p.eliminar(id)
    flash('Se ha eliminado la percepción con éxito!!')
    return redirect(url_for('percepciones'))

#######################################################################################################################
@app.route('/deducciones')
def deducciones():
    d = Deducciones()
    deducciones = d.consultaGeneral()
    return render_template('deducciones/deduccionesListado.html',deducciones = deducciones)

@app.route('/deduccionesNuevo')
def deduccionesNuevo():
    return render_template('deducciones/deduccionesNuevo.html')

@app.route('/registrarDeduccion',methods=['post'])
def registrarDeduccion():
    d = Deducciones()
    d.nombre = request.form['nombre']
    d.descripcion = request.form['descripcion']
    d.porcentaje = request.form['porcentaje']
    d.insertar()
    flash('Se ha registrado un nueva deducción con éxito!!')
    return render_template('deducciones/deduccionesNuevo.html')

@app.route('/deduccionesEditar/<int:id>')
def deduccionesEditar(id):
    d = Deducciones()
    return render_template('deducciones/deduccionesEditar.html', deduccion = d.consultaIndividual(id))

@app.route('/guardarDeduccion',methods=['post'])
def guardarDeduccion():
    d = Deducciones()
    d.idDeduccion = request.form['idDeduccion']
    d.nombre = request.form['nombre']
    d.descripcion = request.form['descripcion']
    d.porcentaje = request.form['porcentaje']
    d.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('deducciones/deduccionesEditar.html', deduccion = d.consultaIndividual(request.form['idDeduccion']))

@app.route('/deduccionesEliminar/<int:id>')
def deduccionesEliminar(id):
    d = Deducciones()
    d.eliminar(id)
    flash('Se ha eliminado la deducción con éxito!!')
    return redirect(url_for('deducciones'))

#######################################################################################################################
@app.route('/periodos')
def periodos():
    p = Periodos()
    periodos = p.consultaGeneral()
    return render_template('periodos/periodosListado.html',periodos = periodos)

@app.route('/periodosNuevo')
def periodosNuevo():
    activado = 1
    return render_template('periodos/periodosNuevo.html', activado = activado)

@app.route('/registrarPeriodo',methods=['post'])
def registrarPeriodo():
    p = Periodos()
    p.nombre = request.form['nombre']
    p.fechaInicio = request.form['fechaInicio']
    p.fechaFin = request.form['fechaFin']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        p.estatus=True
    else:
        p.estatus=False
    p.insertar()
    activado = 1
    flash('Se ha registrado un nuevo periodo con éxito!!')
    return render_template('periodos/periodosNuevo.html', activado = activado)

@app.route('/periodosEditar/<int:id>')
def periodosEditar(id):
    p = Periodos()
    return render_template('periodos/periodosEditar.html', periodo = p.consultaIndividual(id))

@app.route('/guardarPeriodo',methods=['post'])
def guardarPeriodo():
    p = Periodos()
    p.idPeriodo = request.form['idPeriodo']
    p.nombre = request.form['nombre']
    p.fechaInicio = request.form['fechaInicio']
    p.fechaFin = request.form['fechaFin']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        p.estatus=True
    else:
        p.estatus=False
    p.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('periodos/periodosEditar.html', periodo = p.consultaIndividual(request.form['idPeriodo']))

@app.route('/periodosEliminar/<int:id>')
def periodosEliminar(id):
    p = Periodos()
    p.eliminar(id)
    flash('Se ha eliminado el periodo con éxito!!')
    return redirect(url_for('periodos'))

#######################################################################################################################
@app.route('/formasPago')
def formasPago():
    f = FormasPago()
    formasPago = f.consultaGeneral()
    return render_template('formasPago/formasPagoListado.html',formasPago = formasPago)

@app.route('/formasPagoNuevo')
def formasPagoNuevo():
    activado = 1
    return render_template('formasPago/formasPagoNuevo.html', activado = activado)

@app.route('/registrarformaPago',methods=['post'])
def registrarformaPago():
    f = FormasPago()
    f.nombre = request.form['nombre']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        f.estatus=True
    else:
        f.estatus=False
    f.insertar()
    activado = 1
    flash('Se ha registrado una nueva forma de pago con éxito!!')
    return render_template('formasPago/formasPagoNuevo.html', activado = activado)

@app.route('/formasPagoEditar/<int:id>')
def formasPagoEditar(id):
    f = FormasPago()
    return render_template('formasPago/formasPagoEditar.html', formaPago = f.consultaIndividual(id))

@app.route('/guardarformaPago',methods=['post'])
def guardarformaPago():
    f = FormasPago()
    f.idFormaPago = request.form['idFormaPago']
    f.nombre = request.form['nombre']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        f.estatus=True
    else:
        f.estatus=False
    f.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('formasPago/formasPagoEditar.html', formaPago = f.consultaIndividual(request.form['idFormaPago']))

@app.route('/formasPagoEliminar/<int:id>')
def formasPagoEliminar(id):
    f = FormasPago()
    f.eliminar(id)
    flash('Se ha eliminado la forma de pago con éxito!!')
    return redirect(url_for('formasPago'))

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

