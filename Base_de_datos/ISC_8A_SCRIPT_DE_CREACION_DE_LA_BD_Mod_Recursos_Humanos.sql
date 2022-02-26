/*==============================================================*/
/* INTEGRANTES DEL EQUIPO #1                        GRUPO: 8voA */
/*==============================================================*/
/*
CECILIA RODRÍGUEZ RODRÍGUEZ
JORGE ALEJANDRO ORTEGA CAZARES
ANTONIO MORENO MAGALLÓN
RICARDO PAHUA SERVÍN
*/
/*==============================================================*/
/*==============================================================*/

/*==============================================================*/
/* CREACIÓN DE LA BD Mod_Recursos_Humanos                       */
/*==============================================================*/
create database Mod_Recursos_Humanos;
use Mod_Recursos_Humanos;

/*==============================================================*/
/* Tabla: Estados                                               */
/*==============================================================*/
create table Estados(
	idEstado int auto_increment not null,
    nombre varchar(60) not null,
    siglas varchar(10) not null,
    estatus bool not null,
    constraint PK_Estados primary key (idEstado),
    constraint UK_nombreEstados unique (nombre),
    constraint UK_siglasEstados unique (siglas)
);

/*==============================================================*/
/* Tabla: Ciudades                                              */
/*==============================================================*/
create table Ciudades(
	idCiudad int auto_increment not null,
    nombre varchar(80) not null,
    idEstado int not null,
    estatus bool not null,
    constraint PK_Ciudades primary key (idCiudad),
    constraint UK_nombreCiudades unique (nombre)
);

/*==============================================================*/
/* Tabla: Sucursales                                            */
/*==============================================================*/
create table Sucursales(
	idSucursal int auto_increment not null,
    nombre varchar(50) not null,
    telefono varchar(15) not null,
    direccion varchar(80) not null,
    colonia varchar(50) not null,
    codigoPostal varchar(5) not null,
    presupuesto float not null,
    estatus bool not null,
    idCiudad int not null,
    constraint PK_Sucursales primary key (idSucursal),
    constraint UK_nombreSucursales unique (nombre),
    constraint UK_telefonoSucursales unique (telefono),
    constraint UK_direccionSucursales unique (direccion)
);

/*==============================================================*/
/* Tabla: Empleados                                             */
/*==============================================================*/
create table Empleados(
	idEmpleado int auto_increment not null,
    nombre varchar(30) not null,
    apellidoPaterno varchar(30) not null,
    apellidoMaterno varchar(30) not null,
    sexo char not null,
    fechaNacimiento date not null,
    curp varchar(20) not null,
    estadoCivil varchar(20) not null,
    fechaContratacion date not null,
    salarioDiaro float not null,
    nss varchar(10) not null,
    diasVaciones int not null,
    diasPermiso int not null,
    fotografia mediumblob,
    direccion varchar(80) not null,
    colonia varchar(50) not null,
    codigoPostal varchar(5) not null,
    escolaridad varchar(80) not null,
    especialidad varchar(100) not null,
    email varchar(100) not null,
    clave varchar(20) not null,
    tipo varchar(10) not null,
    estatus bool not null,
    idDepartamento int not null,
    idPuesto int not null,
    idCiudad int not null,
    idSucursal int not null,
    idTurno int not null,
    constraint PK_Empleados primary key (idEmpleado),
    constraint UK_nombreEmpleado unique (nombre, apellidoPaterno, apellidoMaterno),
    constraint UK_curpEmpleado unique (curp),
    constraint UK_nssEmpleado unique (nss),
    constraint UK_emailEmpleado unique (email)
);

/*==============================================================*/
/* Tabla: Asistencias                                           */
/*==============================================================*/
create table Asistencias (
	idAsistencia int auto_increment not null,
	fecha date not null,
	horaEntrada time not null,
	horaSalida time not null,
	dia varchar (10) not null,
    idEmpleado int not null,
	constraint Pk_Asistencias primary key (idAsistencia)
);

/*==============================================================*/
/* Tabla: Turnos                                                */
/*==============================================================*/
create table Turnos (
	idTurno int auto_increment not null,
	nombre varchar(20) not null,
	horaInicio time not null,
	horaFin time not null,
	dias varchar (30) not null,
	constraint Pk_Turnos primary key (idTurno),
    constraint UK_nombreTurnos unique (nombre)    
);

/*==============================================================*/
/* Tabla: Departamentos                                         */
/*==============================================================*/
create table Departamentos(
	idDepartamento int auto_increment not null,
    nombre varchar(50) not null,
    estatus bool not null,
    constraint PK_Departamentos primary key (idDepartamento),
    constraint UK_nombreDepartamentos unique(nombre)
);

/*==============================================================*/
/* Tabla: Puestos                                               */
/*==============================================================*/
create table Puestos(
	idPuesto int auto_increment not null,
    nombre varchar(60) not null,
    salarioMinimo float not null,
    salarioMaximo float not null,
    estatus bool not null,
    constraint PK_Puestos primary key (idPuesto),
    constraint UK_nombrePuestos unique(nombre)
);

/*==============================================================*/
/* Tabla: HistorialPuestos                                      */
/*==============================================================*/
create table HistorialPuestos (
    idEmpleado int not null,
	idPuesto int not null,
    idDepartamento int not null,
	fechaInicio date not null,
	fechaFin date not null,	
	constraint Pk_HistorialPuestos primary key (idEmpleado,idPuesto,idDepartamento,fechaInicio)
);

/*==============================================================*/
/* Tabla: AusenciasJustificadas                                 */
/*==============================================================*/
create table AusenciasJustificadas (
	idAusencia int auto_increment not null,
    fechaSolicitud date not null,
    fechaInicio date not null,
	fechaFin date not null,
    tipo char not null,
    idEmpleadoSolicita int not null,
    idEmpleadoAutoriza int not null,
	evidencia blob not null,
	estatus bool not null,
    motivo varchar(100) not null,
	constraint Pk_AsenciasJustificadas primary key (idAusencia)
);

/*==============================================================*/
/* Tabla: DocumentacionEmpleado                                 */
/*==============================================================*/
create table  DocumentacionEmpleado (
    idDocumento int auto_increment not null,
    nombreDocumento varchar(80) not null,
	fechaEntrega date not null,
    documento blob not null,
    idEmpleado int not null,	
	constraint Pk_DocumentacionEmpleado primary key (idDocumento),
	constraint UK_nombreDocumento unique (nombreDocumento)
);

/*==============================================================*/
/* Tabla: Percepciones                                          */
/*==============================================================*/
create table Percepciones(
	idPercepcion int auto_increment not null,
    nombre varchar(30) not null,
    descripcion varchar(80) not null,
    diasPagar int not null,
    constraint PK_Percepciones primary key (idPercepcion),
    constraint UK_nombrePercepciones unique (nombre)
);

/*==============================================================*/
/* Tabla: FormasPago                                            */
/*==============================================================*/
create table FormasPago (
    idFormaPago int auto_increment not null,
    nombre varchar(50) not null,
    estatus bool not null,	
	constraint Pk_FormasPago primary key (idFormaPago),
    constraint UK_nombreFormasPago unique (nombre)
);

/*==============================================================*/
/* Tabla: Periodos                                              */
/*==============================================================*/
create table Periodos(
	idPeriodo int auto_increment not null,
    nombre varchar(50) not null,
    fechaInicio date not null,
    fechaFin date not null,
    estatus bool not null,	
    constraint PK_Periodos primary key (idPeriodo),
    constraint UK_nombrePeriodos unique (nombre)
);

/*==============================================================*/
/* Tabla: Deducciones                                           */
/*==============================================================*/
create table Deducciones(
	idDeduccion int auto_increment not null,
    nombre varchar(30) not null,
    descripcion varchar(80) not null,
    porcentaje float not null,
    constraint PK_Deducciones primary key (idDeduccion),
    constraint UK_nombreDeducciones unique (nombre),
    constraint UK_descripcionDeducciones unique (descripcion)
);

/*==============================================================*/
/* Tabla: NominasPercepciones                                   */
/*==============================================================*/
create table NominasPercepciones(
	idNomina int not null,
    idPercepcion int not null,
    importe float not null,
    constraint PK_NominasPercepciones primary key (idNomina, idPercepcion)
);

/*==============================================================*/
/* Tabla: NominasDeducciones                                    */
/*==============================================================*/
create table NominasDeducciones(
	idNomina int not null,
    idDeduccion int not null,
    importe float not null,
    constraint PK_NominasDeducciones primary key (idNomina, idDeduccion)
);

/*==============================================================*/
/* Tabla: Nominas                                               */
/*==============================================================*/
create table Nominas(
	idNomina int not null,
    fechaElaboracion date not null,
    fechaPago date not null,
    subtotal float not null,
    retenciones float not null,
    total float not null,
    diasTrabajados int not null,
    estatus char not null,
    idEmpleado int not null,
    idPeriodo int not null,
    constraint PK_Nominas primary key(idNomina)
);

/*==============================================================*/
/* Constraints de tipo FK                                       */
/*==============================================================*/
alter table Ciudades add constraint FK_Ciudades_Estados foreign key (idEstado)
      references Estados (idEstado);
alter table Sucursales add constraint FK_Sucursales_Ciudades foreign key (idCiudad)
      references Ciudades (idCiudad);
alter table Asistencias add constraint FK_Asistencias_Empleados foreign key (idEmpleado)
      references Empleados (idEmpleado);
alter table Empleados add constraint FK_Empleados_Ciudades foreign key (idCiudad)
      references Ciudades (idCiudad);
alter table Empleados add constraint FK_Empleados_Turnos foreign key (idTurno)
      references Turnos (idTurno);
alter table Empleados add constraint FK_Empleados_Departamentos foreign key (idDepartamento)
      references Departamentos (idDepartamento);
alter table Empleados add constraint FK_Empleados_Puestos foreign key (idPuesto)
      references Puestos (idPuesto);            
alter table Empleados add constraint FK_Empleados_Sucursales foreign key (idSucursal)
      references Sucursales (idSucursal);
alter table HistorialPuestos add constraint FK_HistorialPuestos_Puestos foreign key (idPuesto)
      references Puestos (idPuesto);
alter table HistorialPuestos add constraint FK_HistorialPuestos_Empleados foreign key (idEmpleado)
      references Empleados (idEmpleado);  
alter table HistorialPuestos add constraint FK_HistorialPuestos_Departamentos foreign key (idDepartamento)
      references Departamentos (idDepartamento);
alter table AusenciasJustificadas add constraint FK_AusenciasJustificadas_Empleados foreign key (idEmpleadoSolicita)
      references Empleados (idEmpleado);  
alter table AusenciasJustificadas add constraint FK_AusenciasJustificadas_Empleados_2 foreign key (idEmpleadoAutoriza)
      references Empleados (idEmpleado); 
alter table DocumentacionEmpleado add constraint FK_DocumentacionEmpleado_Empleados foreign key (idEmpleado)
      references Empleados (idEmpleado); 
alter table NominasDeducciones add constraint FK_NominasDeducciones_Nominas foreign key (idNomina)
      references Nominas (idNomina);  
alter table NominasDeducciones add constraint FK_NominasDeducciones_Deducciones foreign key (idDeduccion)
      references Deducciones (idDeduccion); 
alter table NominasPercepciones add constraint FK_NominasPercepciones_Nominas foreign key (idNomina)
      references Nominas (idNomina);  
alter table NominasPercepciones add constraint FK_NominasPercepciones_Percepciones foreign key (idPercepcion)
      references Percepciones (idPercepcion); 
alter table Nominas add constraint FK_Nominas_FormasPago foreign key (idFormaPago)
      references FormasPago (idFormaPago);  
alter table Nominas add constraint FK_Nominas_Periodos foreign key (idPeriodo)
      references Periodos (idPeriodo); 
alter table Nominas add constraint FK_Nominas_Empleados foreign key (idEmpleado)
      references Empleados (idEmpleado); 
      
/*==============================================================*/
/* Creación de usuario para la BD Mod_Recursos_Humanos          */
/*==============================================================*/
create user userModRecursosHumanos identified by 'Hola.123';
grant insert,update,delete,select on Estados to userModRecursosHumanos;
grant insert,update,delete,select on Ciudades to userModRecursosHumanos;
grant insert,update,delete,select on Sucursales to userModRecursosHumanos;
grant insert,update,delete,select on Asistencias to userModRecursosHumanos;
grant insert,update,delete,select on Empleados to userModRecursosHumanos;
grant insert,update,delete,select on AusenciasJustificadas to userModRecursosHumanos;
grant insert,update,delete,select on Turnos to userModRecursosHumanos;
grant insert,update,delete,select on HistorialPuestos to userModRecursosHumanos; 
grant insert,update,delete,select on Departamentos to userModRecursosHumanos;
grant insert,update,delete,select on FormasPago to userModRecursosHumanos;
grant insert,update,delete,select on DocumentacionEmpleados to userModRecursosHumanos;
grant insert,update,delete,select on Puestos to userModRecursosHumanos;
grant insert,update,delete,select on Percepciones to userModRecursosHumanos;
grant insert,update,delete,select on Periodos to userModRecursosHumanos;
grant insert,update,delete,select on Nominas to userModRecursosHumanos;
grant insert,update,delete,select on NominasPercepciones to userModRecursosHumanos;
grant insert,update,delete,select on NominasDeducciones to userModRecursosHumanos;
grant insert,update,delete,select on Deducciones to userModRecursosHumanos;

