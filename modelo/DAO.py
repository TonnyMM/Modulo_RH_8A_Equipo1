from pickle import FALSE
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey, Float, Time, Date, BLOB
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import datetime
db = SQLAlchemy()


class Empleados(UserMixin,db.Model):
    __tablename__= 'Empleados'
    idEmpleado = Column(Integer, primary_key=True)
    nombre = Column(String(30), unique=True)
    apellidoPaterno = Column(String(30))
    apellidoMaterno = Column(String(30))
    sexo = Column(String, nullable=False)
    fechaNacimiento = Column(Date, nullable=False)
    curp = Column(String(20), nullable=False, unique=True)
    estadoCivil = Column(String(20),nullable=False)
    fechaContratacion = Column(Date, nullable=False,default=datetime.date.today())
    salarioDiaro = Column(Float,nullable=False)
    nss = Column(String(10),nullable=False, unique=True)
    diasVaciones = Column(Integer,nullable=False)
    diasPermiso = Column(Integer,nullable=False)
    fotografia = Column(BLOB)
    direccion = Column(String(80),nullable=False)
    colonia = Column(String(50), nullable=False)
    codigoPostal = Column(String(5), nullable=False)
    escolaridad = Column(String(80), nullable=False)
    especialidad = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    clave = Column(String(20), nullable=False)
    tipo = Column(String(10), nullable=False)
    idDepartamento = Column(Integer,ForeignKey('Departamentos.idDepartamento'))
    idPuesto = Column(Integer,ForeignKey('Puestos.idPuesto'))
    idCiudad = Column(Integer,ForeignKey('Ciudades.idCiudad'))
    idSucursal = Column(Integer,ForeignKey('Sucursales.idSucursal'))
    idTurno = Column(Integer,ForeignKey('Turnos.idTurno'))
    estatus = Column(Boolean, default=True)
    Departamento = relationship('Departamentos',backref='empleados', lazy="select")
    Puesto = relationship('Puestos',backref='empleados', lazy="select")
    Ciudad = relationship('Ciudades',backref='empleados', lazy="select")
    Turno = relationship('Turnos',backref='empleados', lazy="select")

    def consultarEmpleadosCurp(self,curp):
        salida={"estatus":"","mensaje":""}
        estado=None
        estado=self.query.filter(Empleados.curp==curp).first()
        if estado!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="La curp "+curp+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="La curp "+curp+" esta libre."
        return salida
    
    def consultarEmpleadosNss(self,nss):
        salida={"estatus":"","mensaje":""}
        estado=None
        estado=self.query.filter(Empleados.nss==nss).first()
        if estado!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="Este numero  "+nss+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="Este numero "+nss+" esta libre."
        return salida
    def consultarEmpleadoscorre(self,email):
        salida={"estatus":"","mensaje":""}
        estado=None
        estado=self.query.filter(Empleados.email==email).first()
        if estado!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="Este E-mail  "+email+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="Este E-mail "+email+" esta libre."
        return salida

    #METODOS DEL CRUD
    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def validar (self, email, clave):
        empleado=None
        empleado=self.query.filter(Empleados.email==email, Empleados.clave==clave, Empleados.estatus ==True).first()
        return empleado
    
    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Empleados.idEmpleado.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

    #MÉTODOS PARA CUESTIONES DE PERFILAMIENTO
    def is_authenticated(self):
        return True

    def is_active(self):
        return self.estatus

    def get_id(self):
        return self.idEmpleado

    def is_administrador(self):
        if self.tipo=="A":
            return True
        else:
            return False

    def is_staff(self):
        if self.tipo=="S":
            return True
        else:
            return False

    def is_empleado(self):
        if self.tipo=="E":
            return True
        else:
            return False


class Estados(db.Model):
    __tablename__ = 'Estados'
    idEstado=Column(Integer, primary_key=True)
    nombre = Column(String(60), unique=True)
    siglas = Column(String(10), unique=True)
    estatus = Column(Boolean, default=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    
    def consultarEstados(self,nombre):
        salida={"estatus":"","mensaje":""}
        estado=None
        estado=self.query.filter(Estados.nombre==nombre).first()
        if estado!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="El nombre "+nombre+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="El nombre "+nombre+" esta libre."
        return salida
    
    def consultarEstSig(self,siglas):
        salida={"estatus":"","mensaje":""}
        estadosig=None
        estadosig=self.query.filter(Estados.siglas==siglas).first()
        if estadosig!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="Las siglas "+siglas+" ya se encuentran registradas."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="Las siglas "+siglas+" estan libres."
        return salida
    
    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Estados.idEstado.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

class Ciudades(db.Model):
    __tablename__='Ciudades'
    idCiudad=Column(Integer, primary_key=True)
    nombre=Column(String(80), unique=True)
    idEstado=Column(Integer, ForeignKey('Estados.idEstado'))
    estatus=Column(Boolean,default=True)
    Estado=relationship('Estados',backref='ciudades', lazy="select")

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    
    def consultarCiudades(self,nombre):
        salida={"estatus":"","mensaje":""}
        ciudad=None
        ciudad=self.query.filter(Ciudades.nombre==nombre).first()
        if ciudad!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="El nombre "+nombre+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="El nombre "+nombre+" esta libre."
        return salida
    
    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Ciudades.idCiudad.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

    def consultarCiudadEstados(self,id):
        salida=[]

        item=None
        item=self.query.filter(Ciudades.idEstado ==id)
        if item!=None:
            for i in item:
                obj = {"id":"","nombre":""}
                obj["id"]=i.idCiudad
                obj["nombre"]=i.nombre
                salida.append(obj)
        else:
            salida = []
        return salida


class Departamentos(db.Model):
    __tablename__ = 'Departamentos'
    idDepartamento=Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True)
    estatus = Column(Boolean, default=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    
    def consultarDepartamentos(self,nombre):
        salida={"estatus":"","mensaje":""}
        departamento=None
        departamento=self.query.filter(Departamentos.nombre==nombre).first()
        if departamento!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="El nombre "+nombre+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="El nombre "+nombre+" esta libre."
        return salida
    
    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Departamentos.idDepartamento.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

class Puestos(db.Model):
    __tablename__ = 'Puestos'
    idPuesto=Column(Integer, primary_key=True)
    nombre = Column(String(60), unique=True)
    salarioMinimo  = Column(Float)
    salarioMaximo  = Column(Float)
    estatus = Column(Boolean, default=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    
    def consultarPuestos(self,nombre):
        salida={"estatus":"","mensaje":""}
        puesto=None
        puesto=self.query.filter(Puestos.nombre==nombre).first()
        if puesto!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="El nombre "+nombre+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="El nombre "+nombre+" esta libre."
        return salida
    
    def validacionSalario(self,salario, min,max):
        salida={"estatus":"","mensaje":""}
        puesto=None
        if salario<min:
            salida["estatus"]="Error"
            salida["mensaje"]="El salario es muy bajo."
        elif salario>max:
            salida["estatus"]="Error"
            salida["mensaje"]="El salario es muy alto."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="El nombre esta bien."
        return salida
    
    def validarFecha(self,inicio,fin):
        salida={"estatus":"","mensaje":""}
        
        
        if inicio>fin:
            salida["estatus"]="Error"
            salida["mensaje"]="El periodo "+inicio+" "+fin+" no es valido"
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="Este periodo "+inicio+" "+fin+" esta libre."
        return salida
    
    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Puestos.idPuesto.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

class Turnos(db.Model):
    __tablename__ = 'Turnos'
    idTurno = Column(Integer, primary_key=True)
    nombre = Column(String(20), unique=True)
    horaInicio  = Column(Time)
    horaFin  = Column(Time)
    dias = Column(String(30))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    
    def consultarTurnos(self,nombre):
        salida={"estatus":"","mensaje":""}
        turno=None
        turno=self.query.filter(Turnos.nombre==nombre).first()
        if turno!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="El nombre "+nombre+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="El nombre "+nombre+" esta libre."
        return salida
    
    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Turnos.idTurno.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

class Percepciones(db.Model):
    __tablename__ = 'Percepciones'
    idPercepcion = Column(Integer, primary_key=True)
    nombre = Column(String(30), unique=True)
    descripcion = Column(String(80))
    diasPagar = Column(Integer)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    
    def consultarPercepciones(self,nombre):
        salida={"estatus":"","mensaje":""}
        percepcion=None
        percepcion=self.query.filter(Percepciones.nombre==nombre).first()
        if percepcion!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="El nombre "+nombre+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="El nombre "+nombre+" esta libre."
        return salida
    
    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Percepciones.idPercepcion.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

class Deducciones(db.Model):
    __tablename__ = 'Deducciones'
    idDeduccion = Column(Integer, primary_key=True)
    nombre = Column(String(30), unique=True)
    descripcion = Column(String(80),unique=True)
    porcentaje = Column(Float)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    
    def consultarDeducciones(self,nombre):
        salida={"estatus":"","mensaje":""}
        deduccion=None
        deduccion=self.query.filter(Deducciones.nombre==nombre).first()
        if deduccion!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="El nombre "+nombre+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="El nombre "+nombre+" esta libre."
        return salida
    
    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Deducciones.idDeduccion.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

class Periodos(db.Model):
    __tablename__ = 'Periodos'
    idPeriodo = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True)
    fechaInicio = Column(Date)
    fechaFin = Column(Date)
    estatus = Column(Boolean, default=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    
    def consultarPeriodos(self,nombre):
        salida={"estatus":"","mensaje":""}
        periodo=None
        periodo=self.query.filter(Periodos.nombre==nombre).first()
        if periodo!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="El nombre "+nombre+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="El nombre "+nombre+" esta libre."
        return salida
    
    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Periodos.idPeriodo.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

class FormasPago(db.Model):
    __tablename__ = 'FormasPago'
    idFormaPago = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True)
    estatus = Column(Boolean, default=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    
    def consultarFormasPago(self,nombre):
        salida={"estatus":"","mensaje":""}
        formaPago=None
        formaPago=self.query.filter(FormasPago.nombre==nombre).first()
        if formaPago!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="El nombre "+nombre+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="El nombre "+nombre+" esta libre."
        return salida
    
    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(FormasPago.idFormaPago.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

class Sucursales(db.Model):
    __tablename__ = 'Sucursales'
    idSucursal = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True)
    telefono = Column(String(15), unique=True)
    direccion = Column(String(80), unique=True)
    colonia = Column(String(50))
    codigoPostal = Column(String(5))
    presupuesto = Column(Float)
    estatus = Column(Boolean, default=True)
    idCiudad = Column(Integer, ForeignKey('Ciudades.idCiudad'))
    ciudad=relationship('Ciudades',backref='sucursales', lazy="select")

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Sucursales.idSucursal.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion
    
    def consultarSucuNom(self,nombre):
        salida={"estatus":"","mensaje":""}
        estado=None
        estado=self.query.filter(Sucursales.nombre==nombre).first()
        if estado!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="Este nombre de sucursal ya se ha registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="Este nombre "+nombre+" esta libre."
        return salida
    
    def consultarSucuTel(self,telefono):
        salida={"estatus":"","mensaje":""}
        estado=None
        estado=self.query.filter(Sucursales.telefono==telefono).first()
        if estado!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="Este telefono  "+telefono+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="Este telefono "+telefono+" esta libre."
        return salida

    def consultarSucursalesCiudad(self,id):
        salida=[]

        item=None
        item=self.query.filter(Sucursales.idCiudad ==id)
        if item!=None:
            for i in item:
                obj = {"id":"","nombre":""}
                obj["id"]=i.idSucursal
                obj["nombre"]=i.nombre
                salida.append(obj)
        else:
            salida = []
        return salida

class DocumentacionEmpleado(db.Model):
    __tablename__ = 'DocumentacionEmpleado'
    idDocumento = Column(Integer, primary_key=True)
    nombreDocumento = Column(String(80), unique=True)
    fechaEntrega = Column(Date)
    documento = Column(BLOB)
    idEmpleado = Column(Integer, ForeignKey('Empleados.idEmpleado'))
    Empleado=relationship('Empleados',backref='documentos', lazy="select")
    
    def consultarDocu(self,nombreDocumento, idEmpleado):
        salida={"estatus":"","mensaje":""}
        estado=None
        estado=self.query.filter((DocumentacionEmpleado.nombreDocumento==nombreDocumento) , (DocumentacionEmpleado.idEmpleado==idEmpleado)).first()
        if estado!=None:
            salida["estatus"]="Error"
            salida["mensaje"]="La curp "+nombreDocumento+" ya se encuentra registrado."
        else:
            salida["estatus"]="Ok"
            salida["mensaje"]="La curp "+nombreDocumento+" esta libre."
        return salida

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(DocumentacionEmpleado.idDocumento.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

class Asistencias(db.Model):
    __tablename__ = 'Asistencias'
    idAsistencia = Column(Integer, primary_key=True)
    fecha = Column(Date)
    horaEntrada = Column(Date)
    horaSalida = Column(Date)
    dia = Column(String(12))
    estatus = Column(Boolean, default=True)
    idEmpleado = Column(Integer, ForeignKey('Empleados.idEmpleado'))
    Empleado=relationship('Empleados',backref='asistencias', lazy="select")

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(Asistencias.idAsistencia.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion

class AusenciasJustificadas(db.Model):
    __tablename__ = 'AusenciasJustificadas'
    idAusencia = Column(Integer, primary_key=True)
    fechaSolicitud = Column(Date)
    fechaInicio = Column(Date)
    fechaFin = Column(Date)
    tipo = Column(String(15))
    idEmpleadoSolicita = Column(Integer)
    idEmpleadoAutoriza = Column(Integer)
    evidencia = Column(BLOB)
    estatus = Column(String(15))
    motivo = Column(String(100))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(AusenciasJustificadas.idAusencia.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion



class HistorialPuestos(db.Model):
    __tablename__ = 'HistorialPuestos'
    idEmpleado = Column(Integer, ForeignKey('Empleados.idEmpleado'),primary_key=True)
    idPuesto = Column(Integer, ForeignKey('Puestos.idPuesto'),primary_key=True)
    idDepartamento = Column(Integer, ForeignKey('Departamentos.idDepartamento'),primary_key=True)
    fechaInicio = Column(String(50), unique=True)
    fechaFin = Column(String(50), unique=True)
    estatus = Column(Boolean, default=True)
    empleado=relationship('Empleados',backref='empleados', lazy="select")
    puesto=relationship('Puestos',backref='puestos', lazy="select")
    departamento=relationship('Departamentos',backref='departamentos', lazy="select")

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self,idE,idP,idD):
        objeto=self.consultaGeneral()
        ##for hp in objeto:
            ##if hp.idEmpleado == idE and hp.idPuesto==idP and hp.idDepartamento==idD:
                
        return self.query.get((idE,idP,idD))

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        objeto = self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultarPagina(self, pagina):
        paginacion=self.query.order_by(HistorialPuestos.idPuesto.asc()).paginate(pagina,per_page=5,error_out=False)
        return paginacion
    
    def consultarPaginaI(self, pagina):
        paginacion=self.query.order_by(HistorialPuestos.idPuesto.asc()).paginate(pagina,per_page=10,error_out=False)
        return paginacion
    