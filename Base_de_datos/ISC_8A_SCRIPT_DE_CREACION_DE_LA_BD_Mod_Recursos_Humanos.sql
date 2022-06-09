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
    idFormaPago int not null,
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
grant insert,update,delete,select on DocumentacionEmpleado to userModRecursosHumanos;
grant insert,update,delete,select on Puestos to userModRecursosHumanos;
grant insert,update,delete,select on Percepciones to userModRecursosHumanos;
grant insert,update,delete,select on Periodos to userModRecursosHumanos;
grant insert,update,delete,select on Nominas to userModRecursosHumanos;
grant insert,update,delete,select on NominasPercepciones to userModRecursosHumanos;
grant insert,update,delete,select on NominasDeducciones to userModRecursosHumanos;
grant insert,update,delete,select on Deducciones to userModRecursosHumanos;

/*==============================================================*/
/*                          TRIGGERS                            */
/*==============================================================*/

use mod_recursos_humanos
DELIMITER $$
CREATE TRIGGER trigHistorial AFTER INSERT ON mod_recursos_humanos.empleados
 FOR EACH ROW
 BEGIN
	INSERT INTO `mod_recursos_humanos`.`historialpuestos` (`idEmpleado`, `idPuesto`, `idDepartamento`, `fechaInicio`,`estatus`)
    SELECT  idEmpleado, idPuesto,idDepartamento, fechaContratacion,1 FROM mod_recursos_humanos.empleados ORDER BY idEmpleado DESC LIMIT 1;
 END$$
DELIMITER ;

use mod_recursos_humanos
DELIMITER $$
CREATE TRIGGER trigHistorial_Update AFTER UPDATE ON mod_recursos_humanos.empleados FOR EACH ROW
BEGIN
    IF (OLD.idPuesto <> NEW.idPuesto) OR (OLD.idDepartamento <> NEW.idDepartamento)  THEN
		 UPDATE `mod_recursos_humanos`.`historialpuestos`
         SET `fechaFin` = CURDATE() WHERE (`idEmpleado` = OLD.idEmpleado) and (`idPuesto` = OLD.idPuesto) and (`idDepartamento` = OLD.idDepartamento);
		INSERT INTO `mod_recursos_humanos`.`historialpuestos` (`idEmpleado`, `idPuesto`, `idDepartamento`, `fechaInicio`,`estatus`) VALUES (NEW.idEmpleado, NEW.idPuesto, NEW.idDepartamento, CURDATE(),1);
    END IF;
END$$
DELIMITER ;

use mod_recursos_humanos
DELIMITER $$
CREATE TRIGGER trigHistorial_Delete AFTER UPDATE ON mod_recursos_humanos.empleados FOR EACH ROW
BEGIN
    IF (OLD.estatus <> NEW.estatus) THEN
		 UPDATE `mod_recursos_humanos`.`historialpuestos`
         SET `fechaFin` = CURDATE() WHERE (`idEmpleado` = OLD.idEmpleado) and (`idPuesto` = OLD.idPuesto) and (`idDepartamento` = OLD.idDepartamento);
	END IF;
END$$
DELIMITER ;


/*==============================================================*/
/*                     REGISTROS INICIALES                      */
/*==============================================================*/

INSERT INTO `mod_recursos_humanos`.`estados` (`idEstado`, `nombre`, `siglas`, `estatus`) VALUES ('1', 'Aguascalientes ', 'AGS.', '1');
INSERT INTO `mod_recursos_humanos`.`estados` (`idEstado`, `nombre`, `siglas`, `estatus`) VALUES ('2', 'Baja California ', 'B.C.', '1');
INSERT INTO `mod_recursos_humanos`.`estados` (`idEstado`, `nombre`, `siglas`, `estatus`) VALUES ('3', 'México', 'MEX', '1');
INSERT INTO `mod_recursos_humanos`.`estados` (`idEstado`, `nombre`, `siglas`, `estatus`) VALUES ('4', 'Michoacán ', 'MICH', '1');
INSERT INTO `mod_recursos_humanos`.`estados` (`idEstado`, `nombre`, `siglas`, `estatus`) VALUES ('5', 'Querétaro', 'QRO', '1');

INSERT INTO `mod_recursos_humanos`.`ciudades` (`idCiudad`, `nombre`, `idEstado`, `estatus`) VALUES ('1', 'Vista Hermosa', '3', '1');
INSERT INTO `mod_recursos_humanos`.`ciudades` (`idCiudad`, `nombre`, `idEstado`, `estatus`) VALUES ('2', 'Zamora', '4', '1');
INSERT INTO `mod_recursos_humanos`.`ciudades` (`idCiudad`, `nombre`, `idEstado`, `estatus`) VALUES ('3', 'Queretaro', '5', '1');
INSERT INTO `mod_recursos_humanos`.`ciudades` (`idCiudad`, `nombre`, `idEstado`, `estatus`) VALUES ('4', 'La Paz', '2', '1');
INSERT INTO `mod_recursos_humanos`.`ciudades` (`idCiudad`, `nombre`, `idEstado`, `estatus`) VALUES ('5', 'Aguascalientes', '1', '1');

INSERT INTO `mod_recursos_humanos`.`puestos` (`idPuesto`, `nombre`, `salarioMinimo`, `salarioMaximo`, `estatus`) VALUES ('1', 'Contador', '150', '300', '1');
INSERT INTO `mod_recursos_humanos`.`puestos` (`idPuesto`, `nombre`, `salarioMinimo`, `salarioMaximo`, `estatus`) VALUES ('2', 'Secretaria', '100', '350', '1');
INSERT INTO `mod_recursos_humanos`.`puestos` (`idPuesto`, `nombre`, `salarioMinimo`, `salarioMaximo`, `estatus`) VALUES ('3', 'Administracion', '200', '400', '1');
INSERT INTO `mod_recursos_humanos`.`puestos` (`idPuesto`, `nombre`, `salarioMinimo`, `salarioMaximo`, `estatus`) VALUES ('4', 'Gerente', '300', '600', '1');
INSERT INTO `mod_recursos_humanos`.`puestos` (`idPuesto`, `nombre`, `salarioMinimo`, `salarioMaximo`, `estatus`) VALUES ('5', 'Supervisor', '350', '700', '1');

INSERT INTO `mod_recursos_humanos`.`sucursales` (`idSucursal`, `nombre`, `telefono`, `direccion`, `colonia`, `codigoPostal`, `presupuesto`, `estatus`, `idCiudad`) VALUES ('1', 'Sauce', '351-458-8745', 'Foviste', 'Centro', '59648', '15000', '1', '2');
INSERT INTO `mod_recursos_humanos`.`sucursales` (`idSucursal`, `nombre`, `telefono`, `direccion`, `colonia`, `codigoPostal`, `presupuesto`, `estatus`, `idCiudad`) VALUES ('2', '20 de noviembre', '351-456-2587', '20 de noviembre', 'Ejidal', '59647', '15000', '1', '2');
INSERT INTO `mod_recursos_humanos`.`sucursales` (`idSucursal`, `nombre`, `telefono`, `direccion`, `colonia`, `codigoPostal`, `presupuesto`, `estatus`, `idCiudad`) VALUES ('3', 'Jacona', '351-478-2587', 'Jacona', 'Centro', '59641', '16000', '1', '2');
INSERT INTO `mod_recursos_humanos`.`sucursales` (`idSucursal`, `nombre`, `telefono`, `direccion`, `colonia`, `codigoPostal`, `presupuesto`, `estatus`, `idCiudad`) VALUES ('4', 'Acanto', '351-477-5696', 'Fracc Acanto', 'Fracc', '59640', '18000', '1', '2');
INSERT INTO `mod_recursos_humanos`.`sucursales` (`idSucursal`, `nombre`, `telefono`, `direccion`, `colonia`, `codigoPostal`, `presupuesto`, `estatus`, `idCiudad`) VALUES ('5', 'Ecuandureo', '351-478-6241', 'Ecuandureo', 'Centro', '57842', '14000', '1', '2');

INSERT INTO `mod_recursos_humanos`.`percepciones` (`idPercepcion`, `nombre`, `descripcion`, `diasPagar`) VALUES ('1', 'Sueldo', 'Pago al empleado por los dias laborados a la semana', '7');
INSERT INTO `mod_recursos_humanos`.`percepciones` (`idPercepcion`, `nombre`, `descripcion`, `diasPagar`) VALUES ('2', 'Prevision social', 'incluye gastos funerarios, fondo de ahorro, vales de despensa', '10');
INSERT INTO `mod_recursos_humanos`.`percepciones` (`idPercepcion`, `nombre`, `descripcion`, `diasPagar`) VALUES ('3', 'Subsidio', 'se paga a quienes reciben un salario bajo', '7');
INSERT INTO `mod_recursos_humanos`.`percepciones` (`idPercepcion`, `nombre`, `descripcion`, `diasPagar`) VALUES ('4', 'Primas', 'representan beneficios extras en dinero que se pagan al empleado', '7');
INSERT INTO `mod_recursos_humanos`.`percepciones` (`idPercepcion`, `nombre`, `descripcion`, `diasPagar`) VALUES ('5', 'Aguinaldo', 'En el mes de diciembre', '30');

INSERT INTO `mod_recursos_humanos`.`deducciones` (`idDeduccion`, `nombre`, `descripcion`, `porcentaje`) VALUES ('1', 'Pago a sindicato', 'En ocasiones el empleo se consigue a través de la gestión sindical', '5');
INSERT INTO `mod_recursos_humanos`.`deducciones` (`idDeduccion`, `nombre`, `descripcion`, `porcentaje`) VALUES ('2', 'El pago la seguridad social', 'Que es un aporte que no debe superar el 6,7', '5');
INSERT INTO `mod_recursos_humanos`.`deducciones` (`idDeduccion`, `nombre`, `descripcion`, `porcentaje`) VALUES ('3', 'El pago de deuda a la empresa', 'Las empresas pueden prestar dinero a sus empleados', '5');
INSERT INTO `mod_recursos_humanos`.`deducciones` (`idDeduccion`, `nombre`, `descripcion`, `porcentaje`) VALUES ('4', 'Pago fondo retiro', 'Algunas empresas ofrecen aportacion voluntaria ', '4');
INSERT INTO `mod_recursos_humanos`.`deducciones` (`idDeduccion`, `nombre`, `descripcion`, `porcentaje`) VALUES ('5', 'Pago ISR', 'Se descuenta del sueldo bruto', '5');

INSERT INTO `mod_recursos_humanos`.`turnos` (`idTurno`, `nombre`, `horaInicio`, `horaFin`, `dias`) VALUES ('1', 'Matutino', '06:00:00', '14:00:00', 'Lunes-Viernes');
INSERT INTO `mod_recursos_humanos`.`turnos` (`idTurno`, `nombre`, `horaInicio`, `horaFin`, `dias`) VALUES ('2', 'Vespertino', '14:00:00', '22:00:00', 'Lunes - sabado');
INSERT INTO `mod_recursos_humanos`.`turnos` (`idTurno`, `nombre`, `horaInicio`, `horaFin`, `dias`) VALUES ('3', 'Nocturno', '20:00:00', '04:00:00', 'Lunes-Viernes');
INSERT INTO `mod_recursos_humanos`.`turnos` (`idTurno`, `nombre`, `horaInicio`, `horaFin`, `dias`) VALUES ('4', 'Mañana', '06:00:00', '15:00:00', 'Lunes-Miercoles');
INSERT INTO `mod_recursos_humanos`.`turnos` (`idTurno`, `nombre`, `horaInicio`, `horaFin`, `dias`) VALUES ('5', 'Tarde', '14:00:00', '22:00:00', 'Lunes - sabado');

INSERT INTO `mod_recursos_humanos`.`departamentos` (`idDepartamento`, `nombre`, `estatus`) VALUES ('1', 'Ventas', '1');
INSERT INTO `mod_recursos_humanos`.`departamentos` (`idDepartamento`, `nombre`, `estatus`) VALUES ('2', 'Compras', '1');
INSERT INTO `mod_recursos_humanos`.`departamentos` (`idDepartamento`, `nombre`, `estatus`) VALUES ('3', 'Administración', '1');
INSERT INTO `mod_recursos_humanos`.`departamentos` (`idDepartamento`, `nombre`, `estatus`) VALUES ('4', 'Almacén', '1');
INSERT INTO `mod_recursos_humanos`.`departamentos` (`idDepartamento`, `nombre`, `estatus`) VALUES ('5', 'Gerencia', '1');

INSERT INTO `mod_recursos_humanos`.`empleados` (`idEmpleado`, `nombre`, `apellidoPaterno`, `apellidoMaterno`, `sexo`, `fechaNacimiento`, `curp`, `estadoCivil`, `fechaContratacion`, `salarioDiaro`, `nss`, `diasVaciones`, `diasPermiso`, `direccion`, `colonia`, `codigoPostal`, `escolaridad`, `especialidad`, `email`, `clave`, `tipo`, `estatus`, `idDepartamento`, `idPuesto`, `idCiudad`, `idSucursal`, `idTurno`) VALUES ('1', 'Luz María', 'Rodríguez', 'Diaz', 'F', '1966-04-01', 'RODL660401MJCDDAC1', 'Casado', '1966-04-01', '300', '2925412768', '3', '3', 'B. Juárez', 'Las Lomas', '59114', 'Maestria', 'Administración y gestión de empresas', 'luzrodi20@gmail.com', 'Hola.123', 'S', '1', '1', '3', '1', '1', '1');
INSERT INTO `mod_recursos_humanos`.`empleados` (`idEmpleado`, `nombre`, `apellidoPaterno`, `apellidoMaterno`, `sexo`, `fechaNacimiento`, `curp`, `estadoCivil`, `fechaContratacion`, `salarioDiaro`, `nss`, `diasVaciones`, `diasPermiso`, `direccion`, `colonia`, `codigoPostal`, `escolaridad`, `especialidad`, `email`, `clave`, `tipo`, `estatus`, `idDepartamento`, `idPuesto`, `idCiudad`, `idSucursal`, `idTurno`) VALUES ('2', 'Juan', 'Mares', 'Cruz', 'M', '1966-04-01', 'RODL660401MJCDDA23', 'Casado', '1976-05-01', '300', '2925412768', '3', '3', 'B. Juárez', 'Las Lomas', '59114', 'Maestria', 'Administración y gestión de empresas', 'juanesmares@gmail.com', 'Hola.123', 'E', '1', '2', '3', '1', '1', '1');
INSERT INTO `mod_recursos_humanos`.`empleados` (`idEmpleado`, `nombre`, `apellidoPaterno`, `apellidoMaterno`, `sexo`, `fechaNacimiento`, `curp`, `estadoCivil`, `fechaContratacion`, `salarioDiaro`, `nss`, `diasVaciones`, `diasPermiso`, `direccion`, `colonia`, `codigoPostal`, `escolaridad`, `especialidad`, `email`, `clave`, `tipo`, `estatus`, `idDepartamento`, `idPuesto`, `idCiudad`, `idSucursal`, `idTurno`) VALUES ('3', 'Cecilia', 'Rodríguez', 'Rodríguez', 'F', '2000-03-03', 'RORC000103MJCDDCA1', 'Soltera', '2019-04-01', '500', '6816000041', '8', '3', ' Av. La caldera #23', 'Centro', '59220', 'Licenciatura', 'Sistemas computacionales', 'cecilia10rdz@gmail.com', 'Hola.123', 'A', '1', '3', '3', '39', '9', '1');

