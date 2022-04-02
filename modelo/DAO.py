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
    estatus = Column(Boolean, default=True)

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



