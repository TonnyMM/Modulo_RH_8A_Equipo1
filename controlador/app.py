from cgitb import html
import re
from flask import Flask,render_template,request,flash,redirect,url_for,abort
import jinja2
from flask_bootstrap import Bootstrap
from mysqlx import OperationalError
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
import pandas as pd
from pandas import ExcelWriter
import calendar
from tkinter import *
from tkinter import filedialog
from xhtml2pdf import pisa
from jinja2 import Template #Nuevo!
import random
import os
from cmath import pi
from requests import delete

from modelo.DAO import db, Ciudades, Estados, Departamentos, Puestos, Turnos, Percepciones, Deducciones, Periodos, FormasPago, Empleados, Sucursales, DocumentacionEmpleado, Asistencias, AusenciasJustificadas,HistorialPuestos,Nominas,NominasPercepciones,NominasDeducciones
from flask_login import login_required,login_user,logout_user,current_user,LoginManager

app = Flask(__name__, template_folder='../vista', static_folder='../static')
Bootstrap(app)
import json

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://userModRecursosHumanos:Hola.123@localhost/Mod_Recursos_Humanos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'

login_manager= LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
login_manager.login_message = u"Debes iniciar sesión !"
@login_manager.user_loader

def load_user(id):
    return Empleados.query.get(int(id))


@app.route('/')
def login():
    return render_template('comunes/login.html')


#######################################################################################################################
@app.route('/recopilarDatosLogin',methods=['post'])
def validarUsuario():
    empleado= Empleados()
    email = request.form['email']
    clave = request.form['password']
    empleado.validar(email,clave)
    empleado = empleado.validar(email, clave)
    if empleado != None:
        login_user(empleado)
        return render_template('comunes/index.html')
    else:
        flash('¡ Datos incorrectos !')
        return render_template('comunes/login.html')

@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    logout_user()
    return redirect(url_for('login'))

@app.route('/empleados/imagen/<int:id>')
@login_required
def consultarImagenUsuario(id):
    e = Empleados()
    return e.consultaIndividual(id).fotografia

@app.route('/index')
@login_required
def index():
    return render_template('comunes/index.html')
#######################################################################################################################

@app.route('/empleados/<int:page>')
def empleados(page=1):

    e = Empleados()
    d = Departamentos()
    p = Puestos()
    c = Ciudades()
    s = Sucursales()
    sucursales = s.consultaGeneral()
    t = Turnos()
    turnos = t.consultaGeneral()

    try:
        puestos= p.consultaGeneral()
        ciudadess = c.consultaGeneral()
        departamentos = d.consultaGeneral()
        paginacion=e.consultarPagina(page)
        empleados=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay estados registrados")
        empleados=None
    return render_template('empleados/empleadosListado.html',empleados = empleados,paginas=paginas,pagina=page, puestos=puestos,departamentos=departamentos,ciudadess=ciudadess,sucursales=sucursales,turnos=turnos)


@app.route('/empleados/imagen/<int:id>')
@login_required
def consultarImagenEmpledos(id):

        e = Empleados()
        return e.consultaIndividual(id).foto

@app.route('/empleadosNuevo')
def empleadosNuevo():
    d = Departamentos()
    departamentos = d.consultaGeneral()
    p = Puestos()
    puestos = p.consultaGeneral()
    c = Ciudades()
    ciudades = c.consultaGeneral()
    s = Sucursales()
    sucursales = s.consultaGeneral()
    t = Turnos()
    turnos = t.consultaGeneral()
    e = Estados()
    estados = e.consultaGeneral()
    return render_template('empleados/empleadosNuevo.html',departamentos=departamentos,puestos=puestos,ciudades=ciudades, sucursales=sucursales,turnos=turnos,estados=estados)

@app.route('/registrarEmpleados',methods=['post'])
def registrarEmpleados():
    e = Empleados()
    e.nombre = request.form['nombre']
    e.fotografia = request.files['fotografia'].read()
    e.apellidoPaterno = request.form["apellidoPaterno"]
    e.apellidoMaterno = request.form["apellidoMaterno"]
    e.sexo = request.form["sexo"]
    e.fechaNacimiento = request.form['fechaNacimiento']
    e.curp = request.form["curp"]
    e.estadoCivil = request.form["estadoCivil"]
    e.fechaContratacion = request.form['fechaContratacion']
    e.tipo = request.form['tipo']
    e.salarioDiaro = request.form["salarioDiario"]
    e.nss = request.form["nss"]
    e.diasVaciones = request.form["diasVacaciones"]
    e.diasPermiso = request.form["diasPermiso"]
    e.direccion = request.form["direccion"]
    e.colonia = request.form["colonia"]
    e.codigoPostal = request.form["codigoPostal"]
    e.escolaridad = request.form["escolaridad"]
    e.especialidad = request.form["especialidad"]
    e.email = request.form["email"]
    e.clave = request.form["password"]
    e.idDepartamento= request.form["idDepartamento"]
    e.idPuesto= request.form["idPuesto"]
    e.idCiudad= request.form["idCiudad"]
    e.idCiudad = request.form["idCiudad"]
    e.idSucursal = request.form["idSucursal"]
    e.idTurno = request.form["idTurno"]
    e.insertar()
    flash('Se ha registrado un nuevo empleado con éxito!!')
    return render_template('empleados/empleadosNuevo.html')

@app.route('/empleadosEditar/<int:id>')
def empleadosEditar(id):
    e = Empleados()
    d = Departamentos()
    departamentos = d.consultaGeneral()
    p = Puestos()
    puestos = p.consultaGeneral()
    c = Ciudades()
    ciudades = c.consultaGeneral()
    s = Sucursales()
    sucursales = s.consultaGeneral()
    t = Turnos()
    turnos = t.consultaGeneral()
    return render_template('empleados/empleadosEditar.html', empleado = e.consultaIndividual(id),departamentos=departamentos,puestos=puestos,ciudades=ciudades, sucursales=sucursales,turnos=turnos)

@app.route('/guardarEmpleados',methods=['post'])
def guardarEmpleado():
    e = Empleados()
    e.idEmpleado = request.form['idEmpleado']
    e.nombre = request.form['nombre']
    fotografia=request.files['fotografia'].read()
    if fotografia:
        e.fotografia=fotografia
    e.apellidoPaterno = request.form["apellidoPaterno"]
    e.apellidoMaterno = request.form["apellidoMaterno"]
    e.sexo = request.form["sexo"]
    e.fechaNacimiento = request.form['fechaNacimiento']
    e.curp = request.form["curp"]
    e.estadoCivil = request.form["estadoCivil"]
    e.fechaContratacion = request.form['fechaContratacion']
    e.tipo = request.form['tipo']
    e.salarioDiaro = request.form["salarioDiario"]
    e.nss = request.form["nss"]
    e.diasVaciones = request.form["diasVacaciones"]
    e.diasPermiso = request.form["diasPermiso"]
    e.direccion = request.form["direccion"]
    e.colonia = request.form["colonia"]
    e.codigoPostal = request.form["codigoPostal"]
    e.escolaridad = request.form["escolaridad"]
    e.especialidad = request.form["especialidad"]
    e.email = request.form["email"]
    e.clave = request.form["password"]
    e.idDepartamento= request.form["idDepartamento"]
    e.idPuesto= request.form["idPuesto"]
    e.idCiudad= request.form["idCiudad"]
    e.idCiudad = request.form["idCiudad"]
    e.idSucursal = request.form["idSucursal"]
    e.idTurno = request.form["idTurno"]
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        e.estatus=True
    else:
        e.estatus=False
    e.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('empleados/empleadosEditar.html', empleado = e.consultaIndividual(request.form['idEmpleado']))

@app.route('/empleadosEliminar/<int:id>')
def empleadosEliminar(id):
    emp = Empleados()
    e = emp.consultaIndividual(id)
    for empleado in  emp.consultaGeneral():
        if empleado.idEmpleado == id:
            nombre = empleado.nombre
            apellidoPaterno = empleado.apellidoPaterno
            apellidoMaterno = empleado.apellidoMaterno
            sexo = empleado.sexo
            fechaNacimiento = empleado.fechaNacimiento
            curp = empleado.curp
            estadoCivil = empleado.estadoCivil
            fechaContratacion = empleado.fechaContratacion
            tipo = empleado.tipo
            salarioDiaro = empleado.salarioDiaro
            nss = empleado.nss
            diasVaciones = empleado.diasVaciones
            diasPermiso = empleado.diasPermiso
            direccion = empleado.direccion
            colonia = empleado.colonia
            codigoPostal = empleado.codigoPostal
            escolaridad = empleado.escolaridad
            especialidad = empleado.especialidad
            email = empleado.email
            clave = empleado.clave
            idDepartamento = empleado.idDepartamento
            idPuesto = empleado.idPuesto
            idCiudad = empleado.idCiudad
            idSucursal = empleado.idSucursal
            idTurno = empleado.idTurno
            e.idEmpleado = id
            e.nombre = nombre
            e.fotografia = e.fotografia
            e.apellidoPaterno = apellidoPaterno
            e.apellidoMaterno = apellidoMaterno
            e.sexo = sexo
            e.fechaNacimiento = fechaNacimiento
            e.curp = curp
            e.estadoCivil = estadoCivil
            e.fechaContratacion = fechaContratacion
            e.tipo = tipo
            e.salarioDiaro = salarioDiaro
            e.nss = nss
            e.diasVaciones = diasVaciones
            e.diasPermiso = diasPermiso
            e.direccion = direccion
            e.colonia = colonia
            e.codigoPostal = codigoPostal
            e.escolaridad = escolaridad
            e.especialidad = especialidad
            e.email = email
            e.clave = clave
            e.idDepartamento= idDepartamento
            e.idPuesto= idPuesto
            e.idCiudad= idCiudad
            e.idSucursal = idSucursal
            e.idTurno = idTurno
            e.estatus = False
            e.actualizar()
    flash('Se ha eliminado el empleado con éxito!!')
    return redirect(url_for('empleados',page=1))


#######################################################################################################################

@app.route('/estados/<int:page>' )
@login_required
def estados(page=1):
    e = Estados()
    try:

        paginacion=e.consultarPagina(page)
        estados=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay estados registrados")
        estados=None

    return render_template('estados/estadosListado.html',estados = estados,paginas=paginas,pagina=page)

@app.route('/estadosNuevo')
@login_required
def estadosNuevo():
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        return render_template('estados/estadosNuevo.html')
    abort(404)

@app.route('/registrarEstado',methods=['post'])
@login_required
def registrarEstado():
    e = Estados()
    e.nombre = request.form['nombre']
    e.siglas= request.form['siglas']
    e.insertar()
    flash('Se ha registrado un nuevo estado con éxito!!')
    return render_template('estados/estadosNuevo.html')

@app.route('/estadosEditar/<int:id>')
@login_required
def estadosEditar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        e = Estados()
        return render_template('estados/estadosEditar.html', estado = e.consultaIndividual(id))
    else:
        abort(404)

@app.route('/guardarEstado',methods=['post'])
@login_required
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
@login_required
def estadosEliminar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        if current_user.is_authenticated and current_user.is_administrador():
            e = Estados()
            e.eliminar(id)
        else:
            e = Estados()
            e.idEstado = id
            for est in e.consultaGeneral():
                if est.idEstado == id:
                    nombre = est.nombre
                    siglas = est.siglas
            e.nombre = nombre
            e.siglas = siglas
            e.estatus=False
            e.actualizar()
        flash('Se ha eliminado el estado con éxito!!')
        return redirect(url_for('estados',page=1))
    else:
        abort(404)
#######################################################################################################################

@app.route('/ciudades/<int:page>' )
@login_required
def ciudades(page=1):
    c = Ciudades()
    e = Estados ()
    estados = e.consultaGeneral()
    try:

        paginacion=c.consultarPagina(page)
        ciudades=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay ciudades registrados")
        ciudades=None

    return render_template('ciudades/ciudadesListado.html',ciudades = ciudades,paginas=paginas,pagina=page,estados=estados)

@app.route('/ciudadesNuevo')
@login_required
def ciudadesNuevo():
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        e = Estados()
        estados = e.consultaGeneral()
        return render_template('ciudades/ciudadesNuevo.html',estados=estados)
    else:
        abort(404)

@app.route('/registrarCiudad',methods=['post'])
@login_required
def registrarCiudad():
    c = Ciudades()
    c.nombre = request.form['nombre']
    c.idEstado= request.form['idEstado']
    c.insertar()
    flash('Se ha registrado un nueva ciudad con éxito!!')
    return render_template('ciudades/ciudadesNuevo.html')

@app.route('/ciudadesEditar/<int:id>')
@login_required
def ciudadesEditar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        c = Ciudades()
        e = Estados()
        return render_template('ciudades/ciudadesEditar.html', ciudad = c.consultaIndividual(id),estados = e.consultaGeneral())
    else:
        abort(404)
@app.route('/guardarCiudad',methods=['post'])
@login_required
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
@login_required
def ciudadesEliminar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        if current_user.is_authenticated and current_user.is_administrador():
            c = Ciudades()
            c.eliminar(id)
        else:
            c = Ciudades()
            c.idCiudad = id
            for ciudad in c.consultaGeneral():
                if ciudad.idEstado == id:
                    nombre = ciudad.nombre
                    idEstado = ciudad.idEstado
            c.nombre = nombre
            c.idEstado = idEstado
            c.estatus=False
            c.actualizar()
        flash('Se ha eliminado la ciudad con éxito!!')
        return redirect(url_for('ciudades',page=1))
    abort(404)
#######################################################################################################################Ajaxxxxx
@app.route('/empleados/curp/<string:curp>',methods=['get'])
@login_required
def consultarEmpleado(curp):
    empleado=Empleados()
    return json.dumps(empleado.consultarEmpleadosCurp(curp))

@app.route('/empleados/nss/<string:nss>',methods=['get'])
@login_required
def consultarEoNss(nss):
    empleado=Empleados()
    return json.dumps(empleado.consultarEmpleadosNss(nss))

@app.route('/empleados/correo/<string:email>',methods=['get'])
@login_required
def consultarEmails(email):
    empleado=Empleados()
    return json.dumps(empleado.consultarEmpleadoscorre(email))

@app.route('/documento/nombre/<string:nombre>,<int:idEmpleado>',methods=['get'])
@login_required
def consultarDocumento(nombre,idEmpleado):
    docu=DocumentacionEmpleado()

    return json.dumps(docu.consultarDocu(nombre,idEmpleado))

@app.route('/empledo/salario/<int:salario>,<int:idPuesto>',methods=['get'])
@login_required
def consultarsalarioEm(salario,idPuesto):
    puesto=Puestos()
    pue=puesto.consultaIndividual(idPuesto)
    salrioMin=pue.salarioMinimo
    SalarMax=pue.salarioMaximo

    return json.dumps(puesto.validacionSalario(salario,salrioMin,SalarMax))

@app.route('/estado/nombre/<string:nombre>',methods=['get'])
@login_required
def consultarEstado(nombre):
    estado=Estados()
    return json.dumps(estado.consultarEstados(nombre))


@app.route('/estadoSig/siglas/<string:siglas>',methods=['get'])
@login_required
def consultarEstadoSig(siglas):
    estadoSig=Estados()
    return json.dumps(estadoSig.consultarEstSig(siglas))

@app.route('/ciudad/nombre/<string:nombre>',methods=['get'])
@login_required
def consultarCiudad(nombre):
    ciudad=Ciudades()
    return json.dumps(ciudad.consultarCiudades(nombre))


@app.route('/departamento/nombre/<string:nombre>',methods=['get'])
@login_required
def consultarDepartamento(nombre):
    departamento=Departamentos()
    return json.dumps(departamento.consultarDepartamentos(nombre))

@app.route('/puesto/nombre/<string:nombre>',methods=['get'])
@login_required
def consultarPuestos(nombre):
    puesto=Puestos()
    return json.dumps(puesto.consultarPuestos(nombre))

@app.route('/turno/nombre/<string:nombre>',methods=['get'])
@login_required
def consultarTurno(nombre):
    turno=Turnos()
    return json.dumps(turno.consultarTurnos(nombre))

@app.route('/percepcion/nombre/<string:nombre>',methods=['get'])
@login_required
def consultarPercepcion(nombre):
    percepcion=Percepciones()
    return json.dumps(percepcion.consultarPercepciones(nombre))

@app.route('/deduccion/nombre/<string:nombre>',methods=['get'])
@login_required
def consultarDeduccion(nombre):
    deduccion=Deducciones()
    return json.dumps(deduccion.consultarDeducciones(nombre))

@app.route('/periodo/nombre/<string:nombre>',methods=['get'])
@login_required
def consultarPeriodo(nombre):
    periodo=Periodos()
    return json.dumps(periodo.consultarPeriodos(nombre))

@app.route('/formaPago/nombre/<string:nombre>',methods=['get'])
@login_required
def consultarFormaPago(nombre):
    formaPago=FormasPago()
    return json.dumps(formaPago.consultarFormasPago(nombre))

@app.route('/sucursales/nombre/<string:nombre>',methods=['get'])
@login_required
def consultarSucursales(nombre):
    sucu=Sucursales()
    return json.dumps(sucu.consultarSucuNom(nombre))

@app.route('/sucursales/telefono/<string:telefono>',methods=['get'])
@login_required
def consultarSucursalesTel(telefono):
    sucu=Sucursales()
    return json.dumps(sucu.consultarSucuTel(telefono))

@app.route('/fechas/<string:inicio>,<string:fin>',methods=['get'])
@login_required
def consulFechasii(inicio,fin):
    sucu=Puestos()
    return json.dumps(sucu.validarFecha(inicio,fin))

#######################################################################################################################
@app.route('/departamentos/<int:page>' )
@login_required
def departamentos(page=1):
    d = Departamentos()
    try:

        paginacion=d.consultarPagina(page)
        departamento=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay Departamentos registrados")
        departamento=None

    return render_template('departamentos/departamentosListado.html',departamentos = departamento,paginas=paginas,pagina=page)



@app.route('/departamentosNuevo')
@login_required
def departamentosNuevo():
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        activado = 1
        return render_template('departamentos/departamentosNuevo.html',activado=activado)
    else:
        abort(404)
@app.route('/registrarDepartamento',methods=['post'])
@login_required
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
@login_required
def departamentosEditar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        d = Departamentos()
        return render_template('departamentos/departamentosEditar.html', departamento = d.consultaIndividual(id))
    else:
        abort(404)

@app.route('/guardarDepartamento',methods=['post'])
@login_required
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
@login_required
def departamentosEliminar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        if current_user.is_authenticated and current_user.is_administrador():
            d = Departamentos()
            d.eliminar(id)
        else:
            d = Departamentos()
            for dep in d.consultaGeneral():
                if dep.idDepartamento == id:
                    nombre = dep.nombre
            d.idDepartamento=id
            d.nombre=nombre
            d.estatus=False
            d.actualizar()
        flash('Se ha eliminado el departamento con éxito!!')
        return redirect(url_for('departamentos',page=1))
    else:
        abort(404)
#######################################################################################################################

@app.route('/puestos/<int:page>' )
@login_required
def puestos(page=1):
    p = Puestos()
    try:

        paginacion=p.consultarPagina(page)
        puestos=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay Puestos registrados")
        puestos=None

    return render_template('puestos/puestosListado.html',puestos = puestos,paginas=paginas,pagina=page)

@app.route('/puestosNuevo')
@login_required
def puestosNuevo():
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        activado = 1
        correcto= 1
        return render_template('puestos/puestosNuevo.html',activado=activado, correcto =correcto)
    else:
        abort(404)

@app.route('/registrarPuesto',methods=['post'])
@login_required
def registrarPuesto():
    p = Puestos()
    p.nombre = request.form['nombre']
    p.salarioMinimo = request.form['salarioMinimo']
    p.salarioMaximo = request.form['salarioMaximo']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        p.estatus=True
        activado = 1
    else:
        p.estatus=False
        activado = 0
    if p.salarioMinimo<p.salarioMaximo:
        p.insertar()
        flash('Se ha registrado un nuevo puesto con éxito!!')
        return render_template('puestos/puestosNuevo.html', activado=activado,correcto=1)
    else:
        flash('Error!!, el rango de pago fue ingresado incorrectamente!!')
        return render_template('puestos/puestosNuevo.html', activado=activado,correcto=0)

@app.route('/puestosEditar/<int:id>')
@login_required
def puestosEditar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        p = Puestos()
        return render_template('puestos/puestosEditar.html', puesto = p.consultaIndividual(id),correcto = 1)
    else:
        abort(404)

@app.route('/guardarPuesto',methods=['post'])
@login_required
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
    if p.salarioMinimo<p.salarioMaximo:
        p.actualizar()
        flash('Se han guardado los cambios con éxito!!')
        return render_template('puestos/puestosEditar.html', puesto = p.consultaIndividual(request.form['idPuesto']),correcto = 1)
    else:
        flash('Error, el rango de salario ingresado no es válido!!')
        return render_template('puestos/puestosEditar.html', puesto = p.consultaIndividual(request.form['idPuesto']),correcto =0)

@app.route('/puestosEliminar/<int:id>')
@login_required
def puestosEliminar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        if current_user.is_authenticated and current_user.is_administrador():
            p = Puestos()
            p.eliminar(id)
        else:
            p = Puestos()
            for pst in p.consultaGeneral():
                if pst.idPuesto == id:
                    nombre = pst.nombre
                    salarioMinimo = pst.salarioMinimo
                    salarioMaximo = pst.salarioMaximo
            p.idPuesto = id
            p.nombre = nombre
            p.salarioMinimo =salarioMinimo
            p.salarioMaximo = salarioMaximo
            p.estatus = False
            p.actualizar()
        flash('Se ha eliminado el puesto con éxito!!')
        return redirect(url_for('puestos',page=1))
    else:
        abort(404)
#######################################################################################################################


@app.route('/turnos/<int:page>' )
@login_required
def turnos(page=1):
    t = Turnos()
    try:
        paginacion=t.consultarPagina(page)
        turnos=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
           abort(404)
    except OperationalError:
         flash("No hay Turnos registrados")
         turnos=None
    return render_template('turnos/turnosListado.html',turnos = turnos,paginas=paginas,pagina=page)

@app.route('/turnosNuevo/<int:id>')
@login_required
def turnosNuevo(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff):
        return render_template('turnos/turnosNuevo.html',band=id)
    else:
        abort(404)

@app.route('/registrarTurno',methods=['post'])
@login_required
def registrarTurno():
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff):
        t = Turnos()
        t.nombre = request.form['nombre']
        t.horaInicio = request.form['horaInicio']
        t.horaFin = request.form['horaFin']
        dias = ''
        lunes = request.values.get('L',False)
        if lunes=='Lunes':
            dias+=lunes
            dias+=' '
        martes = request.values.get('M',False)
        if martes =='Martes':
            dias+=martes
            dias+=' '
        miercoles = request.values.get('MI',False)
        if miercoles=="Miercoles":
            dias +=miercoles
            dias+=' '
        jueves = request.values.get('J',False)
        if jueves=="Jueves":
            dias +=jueves
            dias+=' '
        viernes = request.values.get('V',False)
        if viernes=="Viernes":
            dias +=viernes
            dias+=' '
        sabado = request.values.get('S',False)
        if sabado=="Sabado":
            dias +=sabado
            dias+=' '
        domingo = request.values.get('D',False)
        if domingo=="Domingo":
            dias +=domingo
            dias+=' '
        t.dias = dias
        t.insertar()
        flash('Se ha registrado un nuevo turno con éxito!!')
        return render_template('turnos/turnosNuevo.html',band=1)
    else:
        abort(404)

@app.route('/turnosEditar/<int:id>')
@login_required
def turnosEditar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff):
        t = Turnos()
        band=1
        turno = t.consultaIndividual(id)
        dias = turno.dias
        ar_dias = dias.split()
        lunes =''
        martes = ''
        miercoles = ''
        jueves = ''
        viernes = ''
        sabado = ''
        domingo = ''
        tam = len(ar_dias)
        l = 0
        for l in ar_dias:
            if l == 'Lunes':
                lunes = l
        for l in ar_dias:
            if l == 'Martes':
                martes = l
        for l in ar_dias:
            if l == 'Miercoles':
                miercoles = l
        for l in ar_dias:
            if l == 'Jueves':
                jueves = l
        for l in ar_dias:
            if l == 'Viernes':
                viernes = l
        for l in ar_dias:
            if l == 'Sabado':
                sabado = l
        for l in ar_dias:
            if l == 'Domingo':
                domingo = l

        return render_template('turnos/turnosEditar.html', turno = t.consultaIndividual(id),band=band,
                               l = lunes,m=martes,mi=miercoles,j=jueves,v=viernes,s=sabado,d=domingo)
    else:
        abort(404)

@app.route('/guardarTurno',methods=['post'])
@login_required
def guardarTurno():
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff):
        t = Turnos()
        t.idTurno = request.form['idTurno']
        t.nombre = request.form['nombre']
        t.horaInicio = request.form['horaInicio']
        t.horaFin = request.form['horaFin']
        dias = ''
        lunes = request.values.get('L',False)
        if lunes=='Lunes':
            dias+=lunes
            dias+=' '
        martes = request.values.get('M',False)
        if martes =='Martes':
            dias+=martes
            dias+=' '
        miercoles = request.values.get('MI',False)
        if miercoles=="Miercoles":
            dias +=miercoles
            dias+=' '
        jueves = request.values.get('J',False)
        if jueves=="Jueves":
            dias +=jueves
            dias+=' '
        viernes = request.values.get('V',False)
        if viernes=="Viernes":
            dias +=viernes
            dias+=' '
        sabado = request.values.get('S',False)
        if sabado=="Sabado":
            dias +=sabado
            dias+=' '
        domingo = request.values.get('D',False)
        if domingo=="Domingo":
            dias +=domingo
            dias+=' '
        t.dias = dias
        t.actualizar()
        flash('Se han guardado los cambios con éxito!!')
        return render_template('turnos/turnosEditar.html', turno = t.consultaIndividual(request.form['idTurno']), band=1,
                               l = lunes,m=martes,mi=miercoles,j=jueves,v=viernes,s=sabado,d=domingo)
    else:
        abort(401)

@app.route('/turnosEliminar/<int:id>')
@login_required
def turnosEliminar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff):
        t = Turnos()
        t.eliminar(id)
        flash('Se ha eliminado el turno con éxito!!')
        return redirect(url_for('turnos',page=1))
    else:
        abort(404)

#######################################################################################################################


@app.route('/percepciones/<int:page>' )
@login_required
def percepciones(page=1):
    p = Percepciones()
    try:

        paginacion=p.consultarPagina(page)
        percepciones=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay percepciones registrados")
        percepciones=None

    return render_template('percepciones/percepcionesListado.html',percepciones = percepciones,paginas=paginas,pagina=page)

@app.route('/percepcionesNuevo')
@login_required
def percepcionesNuevo():
    return render_template('percepciones/percepcionesNuevo.html')

@app.route('/registrarPercepcion',methods=['post'])
@login_required
def registrarPercepcion():
    p = Percepciones()
    p.nombre = request.form['nombre']
    p.descripcion = request.form['descripcion']
    p.diasPagar = request.form['diasPagar']
    p.insertar()
    flash('Se ha registrado un nueva percepcion con éxito!!')
    return render_template('percepciones/percepcionesNuevo.html')

@app.route('/percepcionesEditar/<int:id>')
@login_required
def percepcionesEditar(id):
    p = Percepciones()
    return render_template('percepciones/percepcionesEditar.html', percepcion = p.consultaIndividual(id))

@app.route('/guardarPercepcion',methods=['post'])
@login_required
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
@login_required
def percepcionesEliminar(id):
    p = Percepciones()
    p.eliminar(id)
    flash('Se ha eliminado la percepción con éxito!!')
    return redirect(url_for('percepciones',page=1))

#######################################################################################################################

@app.route('/deducciones/<int:page>' )
@login_required
def deducciones(page=1):
    p = Deducciones()
    try:

        paginacion=p.consultarPagina(page)
        deducciones=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay deducciones registrados")
        deducciones=None
    return render_template('deducciones/deduccionesListado.html',deducciones = deducciones,paginas=paginas,pagina=page)

@app.route('/deduccionesNuevo')
@login_required
def deduccionesNuevo():
    return render_template('deducciones/deduccionesNuevo.html')

@app.route('/registrarDeduccion',methods=['post'])
@login_required
def registrarDeduccion():
    d = Deducciones()
    d.nombre = request.form['nombre']
    d.descripcion = request.form['descripcion']
    d.porcentaje = request.form['porcentaje']
    d.insertar()
    flash('Se ha registrado un nueva deducción con éxito!!')
    return render_template('deducciones/deduccionesNuevo.html')

@app.route('/deduccionesEditar/<int:id>')
@login_required
def deduccionesEditar(id):
    d = Deducciones()
    return render_template('deducciones/deduccionesEditar.html', deduccion = d.consultaIndividual(id))

@app.route('/guardarDeduccion',methods=['post'])
@login_required
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
@login_required
def deduccionesEliminar(id):
    d = Deducciones()
    d.eliminar(id)
    flash('Se ha eliminado la deducción con éxito!!')
    return redirect(url_for('deducciones',page=1))

#######################################################################################################################

@app.route('/periodos/<int:page>' )
@login_required
def periodos(page=1):
    p = Periodos()
    try:

        paginacion=p.consultarPagina(page)
        periodos=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay periodos registrados")
        periodos=None

    return render_template('periodos/periodosListado.html',periodos = periodos,paginas=paginas,pagina=page)

@app.route('/periodosNuevo')
@login_required
def periodosNuevo():
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        activado = 1
        return render_template('periodos/periodosNuevo.html', activado = activado, correcto = 1)
    else:
        abort(404)
@app.route('/registrarPeriodo',methods=['post'])
@login_required
def registrarPeriodo():
    p = Periodos()
    p.nombre = request.form['nombre']
    p.fechaInicio = request.form['fechaInicio']
    p.fechaFin = request.form['fechaFin']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        p.estatus=True
        activado = 1
    else:
        p.estatus=False
        activado = 0
    if p.fechaInicio<p.fechaFin:
        p.insertar()
        flash('Se ha registrado un nuevo periodo con éxito!!')
        return render_template('periodos/periodosNuevo.html', activado = activado,correcto = 1)
    else:
        flash('Error!!, las fechas ingresadas no son válidas')
        return render_template('periodos/periodosNuevo.html', activado = activado,correcto = 0)

@app.route('/periodosEditar/<int:id>')
@login_required
def periodosEditar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        p = Periodos()
        return render_template('periodos/periodosEditar.html', periodo = p.consultaIndividual(id),correcto = 1)
    else:
        abort(404)
@app.route('/guardarPeriodo',methods=['post'])
@login_required
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
    if p.fechaInicio<p.fechaFin:
        p.actualizar()
        flash('Se han guardado los cambios con éxito!!')
        return render_template('periodos/periodosEditar.html', periodo = p.consultaIndividual(request.form['idPeriodo']), correcto = 1)
    else:
        flash('Error!!, las fechas ingresadas no son válidas!!')
        return render_template('periodos/periodosEditar.html', periodo = p.consultaIndividual(request.form['idPeriodo']), correcto = 0)

@app.route('/periodosEliminar/<int:id>')
@login_required
def periodosEliminar(id):
    if current_user.is_authenticated and current_user.is_administrador():
        p = Periodos()
        if current_user.is_authenticated and current_user.is_administrador():
            p.eliminar(id)
        else:
            for per in p.consultaGeneral():
                if per.idPeriodo == id:
                    nombre = per.nombre
                    fechaInicio = per.fechaInicio
                    fechaFin = per.fechaFin
            p.idPeriodo = id
            p.nombre = nombre
            p.fechaInicio = fechaInicio
            p.fechaFin = fechaFin
            p.estatus = False
            p.actualizar()
        flash('Se ha eliminado el periodo con éxito!!')
        return redirect(url_for('periodos',page=1))
    else:
        abort(404)
#######################################################################################################################


@app.route('/formasPago/<int:page>' )
@login_required
def formasPago(page=1):
    if current_user.is_authenticated and (current_user.is_administrador or current_user.is_staff):
        f = FormasPago()
        try:
            paginacion=f.consultarPagina(page)
            formasPago=paginacion.items
            paginas=paginacion.pages
            if paginas < page:
                abort(404)
        except OperationalError:
            flash("No hay formasPago registrados")
            formasPago=None
        return render_template('formasPago/formasPagoListado.html',formasPago = formasPago,paginas=paginas,pagina=page)
    else:
        abort(404)
@app.route('/formasPagoNuevo')
@login_required
def formasPagoNuevo():
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        activado = 1
        return render_template('formasPago/formasPagoNuevo.html', activado = activado)
    else:
        abort(404)

@app.route('/registrarformaPago',methods=['post'])
@login_required
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
@login_required
def formasPagoEditar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        f = FormasPago()
        return render_template('formasPago/formasPagoEditar.html', formaPago = f.consultaIndividual(id))
    else:
        abort(404)

@app.route('/guardarformaPago',methods=['post'])
@login_required
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
@login_required
def formasPagoEliminar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        f = FormasPago()
        if current_user.is_authenticated and current_user.is_administrador():
            f.eliminar(id)
        else:
            for form in f.consultaGeneral():
                if form.idFormaPago == id:
                    nombre = form.nombre
            f.idFormaPago = id
            f.nombre = nombre
            f.estatus = False
            f.actualizar()
        flash('Se ha eliminado la forma de pago con éxito!!')
        return redirect(url_for('formasPago',page=1))
    else:
        abort(404)
#######################################################################################################################
@app.route('/sucursales/<int:page>')
@login_required
def sucursales(page=1):
    s = Sucursales()
    try:
        paginacion=s.consultarPagina(page)
        sucursales=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay sucursales registradas")
        sucursales=None
    return render_template('sucursales/sucursalesListado.html',sucursales = sucursales,paginas=paginas,pagina=page)

@app.route('/sucursalesNuevo')
@login_required
def sucursalesNuevo():
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        activado = 1
        c = Ciudades()
        e = Estados()
        estados = e.consultaGeneral()
        return render_template('sucursales/sucursalesNuevo.html', activado = activado, ciudades = c.consultaGeneral(), estados= estados)
    else:
        abort(404)
@app.route('/registrarSucursal',methods=['post'])
@login_required
def registrarsucursal():
    s = Sucursales()
    s.nombre = request.form['nombre']
    s.telefono=request.form['telefono']
    s.direccion = request.form['direccion']
    s.colonia=request.form['colonia']
    s.codigoPostal = request.form['codigoPostal']
    s.presupuesto=request.form['presupuesto']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        s.estatus=True
        activado = 1
    else:
        s.estatus=False
        activado = 0
    s.idCiudad=request.form['idCiudad']
    s.insertar()
    c = Ciudades()
    flash('Se ha registrado la sucursal con éxito!!')
    return render_template('sucursales/sucursalesNuevo.html', activado = activado, ciudades = c.consultaGeneral())

@app.route('/sucursalesEditar/<int:id>')
@login_required
def sucursalesEditar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        s = Sucursales()
        c = Ciudades()
        return render_template('sucursales/sucursalesEditar.html', sucursal = s.consultaIndividual(id),
                           ciudades = c.consultaGeneral())
    else:
        abort(404)

@app.route('/guardarSucursal',methods=['post'])
@login_required
def guardarSucursal():
    s = Sucursales()
    s.idSucursal = request.form['idSucursal']
    s.nombre = request.form['nombre']
    s.telefono=request.form['telefono']
    s.direccion = request.form['direccion']
    s.colonia=request.form['colonia']
    s.codigoPostal = request.form['codigoPostal']
    s.presupuesto=request.form['presupuesto']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        s.estatus=True
    else:
        s.estatus=False
    s.idCiudad=request.form['idCiudad']
    s.actualizar()
    c = Ciudades()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('sucursales/sucursalesEditar.html',
                           sucursal = s.consultaIndividual(request.form['idSucursal']),ciudades = c.consultaGeneral())

@app.route('/sucursalesEliminar/<int:id>')
@login_required
def sucursalesEliminar(id):
    if current_user.is_authenticated and current_user.is_administrador():
        s = Sucursales()
        if current_user.is_authenticated and current_user.is_administrador():
            s.eliminar(id)
        else:
            for suc in s.consultaGeneral():
                if suc.idSucursal == id:
                    nombre = suc.nombre
                    telefono = suc.telefono
                    direccion = suc.direccion
                    colonia = suc.colonia
                    codigoPostal = suc.codigoPostal
                    presupuesto = suc.presupuesto
                    idCiudad = suc.idCiudad
            s.idSucursal = id
            s.nombre = nombre
            s.telefono =telefono
            s.direccion = direccion
            s.colonia = colonia
            s.codigoPostal = codigoPostal
            s.presupuesto = presupuesto
            s.idCiudad = idCiudad
            s.estatus = False
            s.actualizar()
        flash('Se ha eliminado la sucursal con éxito!!')
        return redirect(url_for('sucursales',page=1))
    else:
        abort(404)
#######################################################################################################################
@app.route('/EmpleadosDocumentacion/<int:page>')
@login_required
def EmpleadosDocumentacion(page=1):
    e = Empleados()
    try:
        paginacion=e.consultarPagina(page)
        empleados=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay Empleados registradas")
        empleados=None
    return render_template('documentacionEmpleados/empleadosDoc.html',empleados = empleados,
                           paginas=paginas,pagina=page)

@app.route('/documentacionEmpleado/<int:page>,<int:id>')
@login_required
def documentacionEmpleado(id,page=1):
    if current_user.is_authenticated and ((current_user.idEmpleado == id) or (current_user.is_administrador() or current_user.is_staff())):
        d = DocumentacionEmpleado()
        e = Empleados()
        return render_template('documentacionEmpleados/documentacionEmpleadoListado.html', empleado = e.consultaIndividual(id),
                               documentacionEmpleado = d.consultaGeneral())
    else:
        abort(404)

@app.route('/documentacionEmpleadoNuevo/<int:id>')
@login_required
def documentacionEmpleadoNuevo(id):
    if current_user.is_authenticated and ((current_user.idEmpleado == id) or (current_user.is_administrador() or current_user.is_staff())):
        e = Empleados()
        fecha = date.today().strftime('%Y-%m-%d')
        return render_template('documentacionEmpleados/documentacionEmpleadoNuevo.html', empleado=e.consultaIndividual(id), fecha = fecha)
    else:
        abort(404)

@app.route('/registrardocumentacionEmpleado',methods=['post'])
@login_required
def registrardocumentacionEmpleado():
    d = DocumentacionEmpleado()
    d.nombreDocumento = request.form['nombreDocumento']
    d.fechaEntrega = request.form['fechaEntrega']
    d.idEmpleado= request.form['idEmpleado']
    d.documento = request.files['documento'].read()
    d.insertar()
    e = Empleados()
    for emp in e.consultaGeneral():
       if emp.idEmpleado == int(request.form['idEmpleado']):
             empleado = emp
    flash('Se ha guardado el documento con éxito!!')
    return render_template('documentacionEmpleados/documentacionEmpleadoNuevo.html', empleado = empleado, fecha =request.form['fechaEntrega'])


@app.route('/documentacionEmpleadoEditar/<int:id>')
@login_required
def documentacionEmpleadoEditar(id):
    doc = DocumentacionEmpleado()
    documento = doc.consultaIndividual(id)
    empleado = documento.idEmpleado
    if current_user.is_authenticated and ((current_user.idEmpleado == empleado) or (current_user.is_administrador() or current_user.is_staff())):
        d = DocumentacionEmpleado()
        return render_template('documentacionEmpleados/documentacionEmpleadoEditar.html', documento = d.consultaIndividual(id))
    else:
        abort(404)


@app.route('/guardardocumentacionEmpleado',methods=['post'])
@login_required
def guardardocumentacionEmpleado():
    doc = DocumentacionEmpleado()
    documento = doc.consultaIndividual(request.form['idDocumento'])
    empleado = documento.idEmpleado
    if current_user.is_authenticated and ((current_user.idEmpleado == empleado) or (current_user.is_administrador() or current_user.is_staff())):
        d = DocumentacionEmpleado()
        d.idDocumento = request.form['idDocumento']
        d.nombreDocumento = request.form['nombreDocumento']
        d.fechaEntrega =request.form['fechaEntrega']
        documento = request.files['documento'].read()
        if documento:
            d.documento = documento
        d.idEmpleado =request.form['idEmpleado']
        d.actualizar()
        flash('Se han guardado los cambios con éxito!!')
        return render_template('documentacionEmpleados/documentacionEmpleadoEditar.html',documento = d.consultaIndividual(request.form['idDocumento']))
    else:
        abort(404)

@app.route('/documentoEliminar/<int:id>')
@login_required
def documentoEliminar(id):
    if current_user.is_authenticated and ((current_user.idEmpleado == id) or (current_user.is_administrador() or current_user.is_staff())):
        d = DocumentacionEmpleado()
        d.eliminar(id)
        flash('Se ha eliminado el documento de forma permanente!!')
        return redirect(url_for('EmpleadosDocumentacion',page=1))
    else:
        abort(404)

@app.route('/empleadoDocumento/<int:id>')
@login_required
def empleadoDocumento(id):
    d = DocumentacionEmpleado()
    return d.consultaIndividual(id).documento

#######################################################################################################################

@app.route('/registrarEntrada')
@login_required
def ventanaregistrarEntrada():
    activado = 1
    fecha = datetime.today().strftime('%Y-%m-%d')
    diaSemana = datetime.today().weekday()
    horaActual = datetime.today().strftime("%H:%M:%S")
    if(diaSemana == 0):
        diaSemana = "Lunes"
    elif(diaSemana == 1):
        diaSemana = "Martes"
    elif (diaSemana == 2):
        diaSemana = "Miercoles"
    elif (diaSemana == 3):
        diaSemana = "Jueves"
    elif (diaSemana == 4):
        diaSemana = "Viernes"
    elif (diaSemana == 5):
        diaSemana = "Sabado"
    elif (diaSemana == 6):
        diaSemana = "Domingo"
    return render_template('asistencias/registraEntrada.html', activado = activado, fecha=fecha,diaSemana=diaSemana,horaActual=horaActual, num = 1)




@app.route('/registrarEntrada',methods=['post'])
def registrarEntrada():
    asistencia = Asistencias()
    asistencia.idEmpleado = request.form['idEmpleado']
    asistencia.fecha = request.form['fecha']

    asistencia.horaEntrada = request.form['horaEntrada']
    asistencia.horaSalida = ""
    fecha = request.form['fecha']
    f2_str = datetime.strptime(fecha, '%Y-%m-%d')
    dia_def= calendar.day_name[f2_str.weekday()]
    if dia_def == 'Monday':
        asistencia.dia = 'Lunes'
    else:
        if dia_def == 'Tuesday':
            asistencia.dia = 'Martes'
        else:
            if dia_def == 'Wednesday':
                asistencia.dia = 'Miercoles'
            else:
                if dia_def == 'Thursday':
                    asistencia.dia = 'Jueves'
                else:
                    if dia_def == 'Friday':
                        asistencia.dia = 'Viernes'
                    else:
                        if dia_def == 'Saturday':
                            asistencia.dia = 'Sabado'
                        else:
                            if dia_def == 'Sunday':
                                asistencia.dia = 'Domingo'


    emp = Empleados()
    datosEmp = emp.consultaIndividual(asistencia.idEmpleado)

    turnos = Turnos()
    datosTurnos = turnos.consultaGeneral()
    listaDias = ""
    turnoactual = ""
    for turno in datosTurnos:
        if(turno.idTurno == datosEmp.idTurno):
            listaDias = turno.dias.split(" ")
            turnoactual = turnos.consultaIndividual(turno.idTurno)

    res = any(ele in asistencia.dia for ele in listaDias) #Devuelve True si el dia actual esta en la lista de dias en el turno del empleado
    if(res):
        horaActual = datetime.strptime(asistencia.horaEntrada,"%H:%M:%S")
        horaturno = datetime.strptime(str(turnoactual.horaInicio),"%H:%M:%S")
        horalimite = horaturno + timedelta(minutes=15)
        if(horaActual >= horaturno and horaActual <= horalimite):
            asistencia.insertar()
            flash('Se ha registrado la asistencia con éxito!!')
        else:
            asistencia.horaSalida = '00:00:00'
            asistencia.insertar()
            flash('Se ha registrado la asistencia con éxito!!')
    else:
        flash('Día no valido!!')

    return redirect(url_for("ventanaregistrarEntrada"))


@app.route('/registrarSalida')
@login_required
def ventanaregistrarSalida():
   
        activado = 1
        fecha = datetime.today().strftime('%Y-%m-%d')
        diaSemana = datetime.today().weekday()
        horaActual = datetime.today().strftime("%H:%M:%S")

        if(diaSemana == 0):
            diaSemana = "Lunes"
        elif(diaSemana == 1):
            diaSemana = "Martes"
        elif (diaSemana == 2):
            diaSemana = "Miercoles"
        elif (diaSemana == 3):
            diaSemana = "Jueves"
        elif (diaSemana == 4):
            diaSemana = "Viernes"
        elif (diaSemana == 5):
            diaSemana = "Sabado"
        elif (diaSemana == 6):
            diaSemana = "Domingo"



        return render_template('asistencias/registraSalida.html', activado = activado, fecha=fecha,diaSemana=diaSemana,horaActual=horaActual)


@app.route('/checarSalidaAsistencia/<int:id>')
@login_required
def checarSalidaAsistencia(id):
    if current_user.is_authenticated():
        asistencia=Asistencias()
        asistencia.horaSalida= datetime.today().strftime("%H:%M") + ":00"
        asistencia.idAsistencia= id
        asistencia.actualizar()
        flash('Asitencia actualizada con exito')
        return redirect(url_for('ventanalistadoAsistencias',page=1))
    else:
        abort(404)
@app.route('/registrarSalida',methods=['post'])
def registrarSalida():
    asistencia = Asistencias()
    asistencia.idEmpleado = request.form['idEmpleado']
    asistencia.horaSalida = request.form['horaSalida']
    asistencia.dia = request.form['diaSemana']
    asistencia.fecha = request.form['fecha']

    datos= asistencia.consultaGeneral()

    emp = Empleados()
    datosEmp = emp.consultaIndividual(asistencia.idEmpleado)

    turnos = Turnos()
    datosTurnos = turnos.consultaGeneral()
    listaDias = ""
    turnoActual = ""

    for elem in datosTurnos:
        if(elem.idTurno == datosEmp.idTurno):
            turnoActual = turnos.consultaIndividual(elem.idTurno)
            listaDias = turnoActual.dias.split(" ")

    idAsistenciaActual = ""
    for x in datos:
        if(str(x.fecha) == str(asistencia.fecha) and str(x.dia) == str(asistencia.dia) and str(asistencia.idEmpleado) == str(current_user.idEmpleado) ):
            idAsistenciaActual = x.idAsistencia
        else:
            flash('Día invalido para registrar salida!!')
            return redirect(url_for("ventanaregistrarSalida"))


    res = any(ele in asistencia.dia for ele in listaDias) #Devuelve True si el dia actual esta en la lista de dias en el turno del empleado

    if(res):
        horaturnoFin = datetime.strptime(str(turnoActual.horaFin),"%H:%M:%S")
        #horaturnoInicio = datetime.strptime(str(turnoActual.horaInicio),"%H:%M:%S")
        horaActual = datetime.strptime(str(asistencia.horaSalida),"%H:%M:%S")
        if(horaActual >= horaturnoFin):
            asistencia.idAsistencia = idAsistenciaActual
            asistencia.horaSalida = request.form['horaSalida']
            asistencia.actualizar()
            flash('Se ha actualizado la asistencia con éxito!!')
        else:
            flash('Horario no valido!!')

    return redirect(url_for("ventanaregistrarSalida"))

@app.route('/asistencias/<int:page>' )
@login_required
def ventanalistadoAsistencias(page=1):
    e = Asistencias()
    for x in e.consultaGeneral():
        print(x.estatus)
    try:
        paginacion=e.consultarPagina(page)
        asistencia=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay estados registrados")
        asistencia=None

    return render_template('asistencias/asistenciasListado.html',asistencia = asistencia,paginas=paginas,pagina=page)



@app.route('/editarAsistencia/<int:id>')
@login_required
def ventanaModificarAsistencia(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        activado = 1
        asistencia = Asistencias()
        datos = asistencia.consultaIndividual(id)
        return render_template('asistencias/modificarAsistencia.html', activado = activado, asistencia=datos)
    else:
        abort(404)

@app.route('/modificarAsistencia',methods=['post'])
def modificarAsistencia():
    asistencia = Asistencias()
    asistencia.idAsistencia = request.form['idAsistencia']
    asistencia.idEmpleado = request.form['idEmpleado']
    fecha = request.form['fecha']
    f2_str = datetime.strptime(fecha, '%Y-%m-%d')
    dia_def= calendar.day_name[f2_str.weekday()]
    if dia_def == 'Monday':
        asistencia.dia = 'Lunes'
    else:
        if dia_def == 'Tuesday':
            asistencia.dia = 'Martes'
        else:
            if dia_def == 'Wednesday':
                asistencia.dia = 'Miercoles'
            else:
                if dia_def == 'Thursday':
                    asistencia.dia = 'Jueves'
                else:
                    if dia_def == 'Friday':
                        asistencia.dia = 'Viernes'
                    else:
                        if dia_def == 'Saturday':
                            asistencia.dia = 'Sabado'
                        else:
                            if dia_def == 'Sunday':
                                asistencia.dia = 'Domingo'
    asistencia.fecha = request.form['fecha']
    asistencia.horaEntrada = request.form['horaInicio']
    asistencia.horaSalida = request.form['horaFin']


    emp = Empleados()
    datosEmp = emp.consultaIndividual(asistencia.idEmpleado)

    turnos = Turnos()
    datosTurnos = turnos.consultaGeneral()
    listaDias = ""

    for elem in datosTurnos:
        if(elem.idTurno == datosEmp.idTurno):
            turnoActual = turnos.consultaIndividual(elem.idTurno)
            listaDias = turnoActual.dias.split(" ")

    res = any(ele in asistencia.dia for ele in listaDias) #Devuelve True si el dia actual esta en la lista de dias en el turno del empleado

    if(res):
       asistencia.actualizar()
       flash('Se ha actualizado la asistencia asistencia con éxito!!')
    return redirect(url_for('ventanalistadoAsistencias',page=1))


@app.route('/asistenciasEliminar/<int:id>')
@login_required
def asistenciasEliminar(id):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        f = Asistencias()
        if current_user.is_authenticated and current_user.is_administrador():
            f.eliminar(id)
        else:
            f.idAsistencia = id
            f.consultaIndividual(id)
            f.estatus = 0
            f.actualizar()
        flash('Se ha eliminado la asistencia con éxito!!')
        return redirect(url_for('ventanalistadoAsistencias',page=1))
    else:
        abort(404)

########################################################################################################################
@app.route('/ausenciasJustificadasListadoGeneral/<int:page>')
@login_required
def AusenciasJust(page=1):
    a = AusenciasJustificadas()
    e = Empleados()
    try:
        paginacion=a.consultarPagina(page)
        ausencias = paginacion.items
        paginas = paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay ausencias justificadas")
        ausencias=None
    asis = a.consultaGeneral()
    return render_template('ausenciasJustificadas/ausenciasJustificadasListado.html',ausenciasJ = ausencias,
                           paginas=paginas,pagina=page, empleados = e.consultaGeneral(), ausencias = asis)


@app.route('/ausenciasJustificadasNuevo')
@login_required
def ausenciasJustificadasNuevo():
    e = Empleados()
    fechaSolicitud = date.today().strftime('%Y-%m-%d')
    rojo = 0
    return render_template('ausenciasJustificadas/ausenciasJustificadasNuevo.html', empleado=e.consultaGeneral(), fechaSolicitud = fechaSolicitud, rojo = rojo)

@app.route('/registrarAusenciasJustificadas',methods=['post'])
@login_required
def registrarAusenciasJustificadas():
    a = AusenciasJustificadas()
    e = Empleados()
    empleado = e.consultaGeneral()
    a.fechaSolicitud = request.form['fechaSolicitud']
    a.fechaInicio = request.form['fechaInicio']
    a.fechaFin = request.form['fechaFin']
    fechai=a.fechaInicio
    fechaf = a.fechaFin
    fi =datetime.strptime(fechai, '%Y-%m-%d')
    fn = datetime.strptime(fechaf, '%Y-%m-%d')
    cont =0
    while fi != fn:
        td = timedelta(1)
        fi = fi + td
        cont = cont + 1

    a.tipo = request.form['tipo']
    a.idEmpleadoSolicita = request.form['idEmpleadoSolicita']
    emp = e.consultaIndividual(str(a.idEmpleadoSolicita))
    diasp = emp.diasPermiso
    diasv = emp.diasVaciones
    a.idEmpleadoAutoriza = request.form['idEmpleadoAutoriza']
    a.motivo = request.form['motivo']
    a.estatus = request.form['estatus']

    valido = 1

    if a.tipo == 'Permiso':
        if diasp < cont:
            valido = 0
    else:
        if a.tipo == 'Periodo Vacacional':
            if diasv < cont:
                valido = 0
    rojo = 0
    if valido == 1:
        a.insertar()
        flash('Se ha guardado el documento con éxito!!')

    else:
        if a.tipo == 'Permiso':
            rojo = 1
            flash('No cuentas con suficientes días!!')
        else:
            if a.tipo == 'Periodo Vacacional':
                rojo = 1
                flash('No cuentas con suficientes días vacacionales!!')
    return render_template('ausenciasJustificadas/ausenciasJustificadasNuevo.html', empleado = empleado, fechaSolicitud = request.form['fechaSolicitud'],rojo=rojo)


@app.route('/ausenciasEditar/<int:id>')
@login_required
def ausenciasEditar(id):
   a = AusenciasJustificadas()
   e = Empleados()
   return render_template('ausenciasJustificadas/ausenciasJustificadasEditar.html', ausencia = a.consultaIndividual(id),
                               empleados = e.consultaGeneral())

@app.route('/guardarAusenciasJustificadas',methods=['post'])
@login_required
def guardarAusenciasJustificadas():
    a = AusenciasJustificadas()
    e = Empleados()
    a.idAusencia = request.form['idAusencia']
    a.fechaSolicitud = request.form['fechaSolicitud']
    a.fechaInicio = request.form['fechaInicio']
    a.fechaFin = request.form['fechaFin']
    a.tipo = request.form['tipo']
    a.idEmpleadoSolicita = request.form['idEmpleadoSolicita']
    a.idEmpleadoAutoriza = request.form['idEmpleadoAutoriza']
    a.evidencia = None
    a.estatus = request.form['estatus']
    a.motivo = request.form['motivo']
    a.actualizar()
    return render_template('ausenciasJustificadas/ausenciasJustificadasEditar.html', ausencia = a.consultaIndividual(request.form['idAusencia']),
                           empleados = e.consultaGeneral())

@app.route('/ausenciasEliminar/<int:id>')
@login_required
def ausenciasEliminar(id):
        a = AusenciasJustificadas()
        aus = a.consultaIndividual(id)
        for au in a.consultaGeneral():
            if au.idAusencia == aus.idAusencia:
                fechaSolicitud = au.fechaSolicitud
                fechaInicio = au.fechaInicio
                fechaFin = au.fechaFin
                tipo = au.tipo
                idEmpleadoSolicita = au.idEmpleadoSolicita
                idEmpleadoAutoriza = au.idEmpleadoAutoriza
                evidencia = au.evidencia
                motivo = au.motivo
        aus.idAusencia = id
        aus.fechaSolicitud = fechaSolicitud
        aus.fechaInicio = fechaInicio
        aus.fechaFin = fechaFin
        aus.tipo = tipo
        aus.idEmpleadoSolicita = idEmpleadoSolicita
        aus.idEmpleadoAutoriza = idEmpleadoAutoriza
        aus.estatus = 'Eliminado'
        aus.evidencia = evidencia
        aus.motivo =motivo
        aus.actualizar()
        flash('Se ha eliminado el documento de forma correcta!!')
        return redirect(url_for('AusenciasJust',page=1))

@app.route('/empleadoEvidencia/<int:id>')
@login_required
def empleadoEvidencia(id):
    a = AusenciasJustificadas()
    return a.consultaIndividual(id).evidencia
##########################################################################################################################################
@app.route('/historialPuestos/<int:page>' )
@login_required
def historialPuestos(page=1):
    h = HistorialPuestos()
    e = Empleados()
    p = Puestos()
    d = Departamentos()
    empleados = e.consultaGeneral()
    puestos = p.consultaGeneral()
    departamentos = d.consultaGeneral()
    try:
        
        paginacion=h.consultarPagina(page)
        hpuestos=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay Puestos registrados")
        hpuestos=None
    
    return render_template('historialPuestos/historialPuestosListado.html',hpuestos = hpuestos,paginas=paginas,pagina=page,empleados=empleados,puestos=puestos,departamentos=departamentos)

@app.route('/historialPuestosEmp/<int:id>,<int:page>' )
@login_required
def historialPuestosEmp(id,page=1):
    h = HistorialPuestos()
    e = Empleados()
    p = Puestos()
    d = Departamentos()
    empleado = e.consultaIndividual(id)
    puestos = p.consultaGeneral()
    departamentos = d.consultaGeneral()
    try:
        
        paginacion=h.consultarPaginaI(page)
        hpuestos=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay Puestos registrados")
        hpuestos=None
    
    return render_template('historialPuestos/historialPuestoEmpListado.html',hpuestos = hpuestos,paginas=paginas,pagina=page,empleado=empleado,puestos=puestos,departamentos=departamentos)

@app.route('/historialPuestosEditar/<int:idE>,<int:idP>,<int:idD>')
@login_required
def historialPuestosEditar(idE,idP,idD):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        hp= HistorialPuestos()
        empl= Empleados()
        puestos=Puestos()
        departamentos=Departamentos()
        historialP=hp.consultaIndividual(idE,idP,idD)
        return render_template('historialPuestos/HistorialEditar.html', historialP = historialP,correcto = 1,empleados=empl.consultaGeneral(),puestos=puestos.consultaGeneral(),departamentos=departamentos.consultaGeneral())
    else:
        abort(404)

@app.route('/historialPuestosEditarIn/<int:idE>,<int:idP>,<int:idD>')
@login_required
def historialPuestosEditarIn(idE,idP,idD):
    if current_user.is_authenticated and (current_user.is_administrador() or current_user.is_staff()):
        hp= HistorialPuestos()
        empl= Empleados()
        puestos=Puestos()
        departamentos=Departamentos()
        historialP=hp.consultaIndividual(idE,idP,idD)
        return render_template('historialPuestos/HistorialIndiEditar.html', historialP = historialP,correcto = 1,empleados=empl.consultaGeneral(),puestos=puestos.consultaGeneral(),departamentos=departamentos.consultaGeneral())
    else:
        abort(404)
@app.route('/guardarHistorial',methods=['post'])
@login_required
def guardarHistorial():
    h = HistorialPuestos()
    empl= Empleados()
    puestos=Puestos()
    departamentos=Departamentos()
    historialP = h.consultaIndividual(request.form['idEmpleado'],request.form['idPuesto'],request.form['idDepartamento'])
    h.idEmpleado = request.form['idEmpleado']
    h.idPuesto = request.form['idPuesto']
    h.idDepartamento = request.form['idDepartamento']
    h.fechaInicio = request.form['fechaInicio']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        h.estatus=True
    else:
        h.estatus=False
    if request.form['fechaFin'] != '':
        h.fechaFin = request.form['fechaFin']
    h.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('historialPuestos/HistorialEditar.html', historialP = historialP, correcto = 1,empleados=empl.consultaGeneral(),puestos=puestos.consultaGeneral(),departamentos=departamentos.consultaGeneral())

@app.route('/guardarHistorialIn',methods=['post'])
@login_required
def guardarHistorialIn():
    h = HistorialPuestos()
    empl= Empleados()
    puestos=Puestos()
    departamentos=Departamentos()
    historialP = h.consultaIndividual(request.form['idEmpleado'],request.form['idPuesto'],request.form['idDepartamento'])
    h.idEmpleado = request.form['idEmpleado']
    h.idPuesto = request.form['idPuesto']
    h.idDepartamento = request.form['idDepartamento']
    h.fechaInicio = request.form['fechaInicio']
    estatus = request.values.get('estatus',False)
    if estatus=="True":
        h.estatus=True
    else:
        h.estatus=False
    if request.form['fechaFin'] != '':
        h.fechaFin = request.form['fechaFin']
    h.actualizar()
    flash('Se han guardado los cambios con éxito!!')
    return render_template('historialPuestos/historialIndiEditar.html', historialP = historialP, correcto = 1,empleados=empl.consultaGeneral(),puestos=puestos.consultaGeneral(),departamentos=departamentos.consultaGeneral())



@app.route('/historialPuestosEliminal/<int:idE>,<int:idP>,<int:idD>')
@login_required
def historialPuestosEliminal(idE,idP,idD):
    
    hp= HistorialPuestos()
    h=hp.consultaIndividual(idE,idP,idD)
    for hh in hp.consultaGeneral():
        if hh.idEmpleado == idE and hh.idPuesto == idP and hh.idDepartamento==idD:
            fechaI=hh.fechaInicio
            fechaf=hh.fechaFin
            h.idEmpleado=idE
            h.idPuesto=idP
            h.idDepartamento=idD
            h.fechaInicio=fechaI
            h.fechaf=fechaf
            h.estatus=False
            h.actualizar()
    
    
    flash('Se ha eliminado el empleado con éxito!!')
    return redirect(url_for('historialPuestos',page=1))

####################################################################################################################
@app.route('/nominas/<int:page>')
def nominas(page=1):
    n = Nominas()
    try:
        paginacion=n.consultarPagina(page)
        nominas=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay nominas registradss")
        nominas=None

    return render_template('nominas/nominasListado.html',nominas = nominas,paginas=paginas,pagina=page)


@app.route('/nominasEmpleados/<int:page>')
def nominasEmpleados(page=1):
    e = Empleados()
    try:
        paginacion=e.consultarPagina(page)
        empleados=paginacion.items
        paginas=paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay empleados registradss")
        empleados=None

    return render_template('nominas/nominasEmpleados.html',empleados = empleados,paginas=paginas,pagina=page)

@app.route('/generarNomina/<int:id>')
def generarNomina(id):
    n = Nominas()
    p = Percepciones()
    fp = FormasPago()
    peri = Periodos()
    percepciones = p.consultaGeneral()
    d = Deducciones()
    deducciones = d.consultaGeneral()
    forma=fp.consultaGeneral()
    periodos=peri.consultaGeneral()
    emp = Empleados()
    empleado = emp.consultaIndividual(id)
    print(id)
    return render_template('nominas/nominasNuevo.html',percepciones=percepciones, deducciones=deducciones,forma=forma,periodos=periodos,
                           empleado = empleado)

@app.route('/registrarNomina',methods=['post'])
def registrarNomina():
    n = Nominas()
    n.fechaPago = request.form['fechaPago']
    n.idFormaPago = request.form['idFormaPago']
    n.idPeriodo = request.form['idPeriodo']
    n.diasTrabajados = request.form['diasTrabajados']
    p = Percepciones()
    fp = FormasPago()
    peri = Periodos()
    percepciones = p.consultaGeneral()
    d = Deducciones()
    deducciones = d.consultaGeneral()
    forma=fp.consultaGeneral()
    periodos=peri.consultaGeneral()
    emp = Empleados()
    empleado = emp.consultaIndividual(request.form['idEmpleado'])
    return render_template('nominas/nominasEditar.html',percepciones=percepciones, deducciones=deducciones,forma=forma,periodos=periodos,
                           empleado = empleado)

@app.route('/nominasPercepciones')
def nominasPercepciones():
    bandera = 1
    n = Nominas()
    p = Percepciones()
    percepciones = p.consultaGeneral()
    d = Deducciones()
    deducciones = d.consultaGeneral()
    nP = NominasPercepciones()
    nominasP = nP.consultaGeneral()
    return render_template('nominas/nominasNuevo.html', percepciones=percepciones, deducciones=deducciones, bandera=bandera,nominasP=nominasP)


@app.route('/nominasDeducciones')
def nominasDeducciones():
    bandera = 1
    n = Nominas()
    p = Percepciones()
    percepciones = p.consultaGeneral()
    d = Deducciones()
    deducciones = d.consultaGeneral()
    nP = NominasDeducciones()
    nominasD = nP.consultaGeneral()
    return render_template('nominas/nominasNuevo.html', percepciones=percepciones, deducciones=deducciones, bandera=bandera,nominasD=nominasD)




#############################################################################################################

@app.route('/sucursalesCiudad/<int:id>',methods=['get'])
def sucursalesCiudad(id):
    item= Sucursales()
    return json.dumps(item.consultarSucursalesCiudad(id))

@app.route('/ciudadesEstado/<int:id>',methods=['get'])
def ciudadesEstado(id):
    item= Ciudades()
    return json.dumps(item.consultarCiudadEstados(id))

########################################################################################################################
@app.route('/generarExcel')
def generarExcel():
    n = Nominas()
    nombre =[]
    puesto = []
    departamento = []
    Curp = []
    nss = []
    fechaElaboracion =[]
    fechaPago = []
    subtotal = []
    retenciones =[]
    total = []
    diasTrabajados = []
    estatus = []
    formaPago = []
    periodo = []
    for nom in n.consultaGeneral():
        if nom.estatus == 'Aceptada' and (current_user.is_administrador() or current_user.is_staff()):
            nombre.append(nom.empleado.nombre+' '+nom.empleado.apellidoPaterno+' '+nom.empleado.apellidoMaterno)
            puesto.append(nom.empleado.Puesto.nombre)
            departamento.append(nom.empleado.Departamento.nombre)
            Curp.append(nom.empleado.curp)
            nss.append(nom.empleado.nss)
            fechaElaboracion.append(nom.fechaElaboracion)
            fechaPago.append(nom.fechaPago)
            subtotal.append(nom.subtotal)
            retenciones.append(nom.retenciones)
            total.append(nom.total)
            diasTrabajados.append(nom.diasTrabajados)
            estatus.append(nom.estatus)
            formaPago.append(nom.formaPago.nombre)
            periodo.append(nom.periodo.nombre)
        else:
            if nom.estatus == 'Aceptada':
                if nom.idEmpleado == current_user.idEmpleado:
                    nombre.append(nom.empleado.nombre+' '+nom.empleado.apellidoPaterno+' '+nom.empleado.apellidoMaterno)
                    puesto.append(nom.empleado.Puesto.nombre)
                    departamento.append(nom.empleado.Departamento.nombre)
                    Curp.append(nom.empleado.curp)
                    nss.append(nom.empleado.nss)
                    fechaElaboracion.append(nom.fechaElaboracion)
                    fechaPago.append(nom.fechaPago)
                    subtotal.append(nom.subtotal)
                    retenciones.append(nom.retenciones)
                    total.append(nom.total)
                    diasTrabajados.append(nom.diasTrabajados)
                    estatus.append(nom.estatus)
                    formaPago.append(nom.formaPago.nombre)
                    periodo.append(nom.periodo.nombre)

    df = pd.DataFrame({'Nombre': nombre,
                       'Puesto': puesto,
                       'Departamento': departamento,
                       'Curp':Curp,
                       'nss':nss,
                       'Fecha de elaboración': fechaElaboracion,
                       'Fecha de pago': fechaPago,
                       'Percepciones': subtotal,
                       'Deducciones': retenciones,
                       'Total': total,
                       'Dias trabajados': diasTrabajados,
                       'Estatus': estatus,
                       'Forma de pago': formaPago,
                       'Periodo': periodo})
    df = df[['Nombre', 'Puesto', 'Departamento','Curp','nss','Periodo','Fecha de pago', 'Forma de pago', 'Fecha de elaboración', 'Dias trabajados', 'Percepciones', 'Deducciones', 'Total']]
    #raiz= Tk()
    #rut = filedialog.askdirectory()
    #raiz.mainloop()
    rut= "C:/Users/cecil/Downloads"
    nomb="/nominas"
    hoy=datetime.now()
    bre=hoy.strftime('%d-%m-%Y')
    nombrearch = nomb+"-"+bre+str(random.randint(1, 20))+".xlsx"

    ruta = rut+nombrearch
    print(ruta)
    writer = ExcelWriter(ruta)
    df.to_excel(writer, 'Hoja de datos', index=False)
    writer.save()

    flash("Se ha gerenerado el Excel y se ha guardado en descargas")
    return redirect(url_for('nominas',page=1))

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sourceHtml = open(os.path.join(base_dir, 'Documentos/solicitudPermisos.html')).read()

@app.route('/pdfPermisos/<int:idE>,<int:idA>,<int:page>')
def pdfPermisos(idE,idA,page):
    e = Empleados()
    a = AusenciasJustificadas()
    p = Puestos()
    d = Departamentos()
    t = Turnos()
    empleados = e.consultaGeneral()
    #print(base_dir)
    #ruta_template = 'D:/Tec/Git/Modulo_RH_8A_Equipo1/vista/Formatos/solicitudPermisos.html'
    empleado = e.consultaIndividual(idE)
    ausencias = a.consultaIndividual(idA)
    pt=p.consultaGeneral()
    dp = d.consultaGeneral()
    tt=t.consultaGeneral()
    dpa=""
    puesto=""
    tn=""
    for pp in pt:
        if empleado.idPuesto == pp.idPuesto:
            puesto=pp.nombre
            
    for d in dp:
        if empleado.idDepartamento == d.idDepartamento:
            dpa=d.nombre
            
    for ti in tt:
        if empleado.idTurno == ti.idTurno:
            tn=ti.nombre
    
    if ausencias.tipo == "Permiso":

        data = {'nombre' :empleado.nombre, 'apellidoPaterno':empleado.apellidoPaterno, 'apellidoMaterno':empleado.apellidoMaterno,
                'fechaSolicitud': ausencias.fechaSolicitud,'nss':empleado.nss, 'turno':tn, 'curp':empleado.curp, 'puesto':puesto,
                'fechaContratacion': empleado.fechaContratacion, 'departamento': dpa, 'nss':empleado.nss, 'fechaInicio': ausencias.fechaInicio,
                'fechaFin':ausencias.fechaFin, 'motivo':ausencias.motivo}
            
        outputFilename = "Solicitud_"+ausencias.tipo+"_"+empleado.nombre+empleado.apellidoPaterno+".pdf"  
        resultFile = open(outputFilename, "w+b")
        template = Template(open(os.path.join(base_dir, 'Documentos/solicitudPermisos.html')).read())
        html  = template.render(data)
        pisaStatus = pisa.CreatePDF(html,dest=resultFile)
        print(resultFile)
        a.idAusencia = idA
        #a.evidencia = open(outputFilename, 'rb').read()
            #open(os.path.join(base_dir, 'controlador/',outputFilename)).read()
        
        resultFile.close()
        a.evidencia = open(outputFilename,'rb').read()
        a.actualizar()
        os.remove(outputFilename)
    
    if ausencias.tipo == "Periodo Vacacional":
    
        data = {'nombre' :empleado.nombre, 'apellidoPaterno':empleado.apellidoPaterno, 'apellidoMaterno':empleado.apellidoMaterno,
                'fechaSolicitud': ausencias.fechaSolicitud,'nss':empleado.nss, 'turno':tn, 'curp':empleado.curp, 'puesto':puesto,
                'fechaContratacion': empleado.fechaContratacion, 'departamento': dpa, 'nss':empleado.nss, 'fechaInicio': ausencias.fechaInicio,
                'fechaFin':ausencias.fechaFin, 'motivo':ausencias.motivo}
            
        outputFilename = "Solicitud_"+ausencias.tipo+"_"+empleado.nombre+empleado.apellidoPaterno+".pdf"    
        resultFile = open(outputFilename, "w+b")
        template = Template(open(os.path.join(base_dir, 'Documentos/solicitudPeriodoVacacional.html')).read())
        html  = template.render(data)
        pisaStatus = pisa.CreatePDF(html,dest=resultFile)
        print(resultFile)
        a.idAusencia = idA
        #a.evidencia = open(outputFilename, 'rb').read()
            #open(os.path.join(base_dir, 'controlador/',outputFilename)).read()
        
        resultFile.close()
        a.evidencia = open(outputFilename,'rb').read()
        a.actualizar()
        os.remove(outputFilename)
        
    try:
        paginacion=a.consultarPagina(page)
        ausencias = paginacion.items
        paginas = paginacion.pages
        if paginas < page:
            abort(404)
    except OperationalError:
        flash("No hay ausencias justificadas")
        ausencias=None
    asis = a.consultaGeneral()
    return render_template('ausenciasJustificadas/ausenciasJustificadasListado.html',ausenciasJ = ausencias,
                           paginas=paginas,pagina=page, empleados = e.consultaGeneral(), ausencias = asis)
        
    


@app.errorhandler(404)
def error404(e):
    return render_template('comunes/paginaError.html'),404



if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
    '''HOST = os.environ.get('SERVER_HOST','172.16.1.65')
    PORT = 5000
    app.run(HOST,PORT)'''
    '''HOST = os.environ.get('SERVER_HOST','localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT','80'))
    except ValueError:
        PORT = 80
    app.run(HOST,PORT)'''
