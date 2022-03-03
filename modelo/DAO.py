from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

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



