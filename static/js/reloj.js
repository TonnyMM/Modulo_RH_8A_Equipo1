(function(){


	var subtotal = document.getElementById('Subtotal').value;
    var dedu = document.getElementById('Retenciones').value;
    var total = subtotal + dedu;
	$('#Total').val(total);

	
	var actualizarHora = function(){
		var fecha = new Date(),
			horas = fecha.getHours(),
			ampm,
			minutos = fecha.getMinutes(),
			segundos = fecha.getSeconds(),
			diaSemana = fecha.getDay(),
			dia = fecha.getDate(),
			mes = fecha.getMonth(),
			year = fecha.getFullYear();	
		var pHoras = document.getElementById('horas'),
			pAMPM = document.getElementById('ampm'),
			pMinutos = document.getElementById('minutos'),
			pSegundos = document.getElementById('segundos'),
			pDiaSemana = document.getElementById('diaSemana'),
			pDia = document.getElementById('dia'),
			pMes = document.getElementById('mes'),
			pYear = document.getElementById('year');

		var semana = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']; 
			pDiaSemana.textContent = semana[diaSemana];

			pDia.textContent = dia;

		var meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']; 
			pMes.textContent =  meses[mes];

			pYear.textContent = year;

		if (horas >= 12) {
			horas = horas - 12;
		   	ampm = 'PM';
		} else{
			ampm = 'AM';
		}

		if (horas == 0) {
			horas = 12;
		}

		pHoras.textContent = horas;
		pAMPM.textContent = ampm;

		if (minutos < 10) { minutos = "0" + minutos }	
		if (segundos < 10) { segundos = "0" + segundos }

		pMinutos.textContent = minutos;
		pSegundos.textContent = segundos;
	};


	actualizarHora();
	var intervalo = setInterval(actualizarHora,1000);
}())

$(function() {
	$('input[type=file]').change(function(){
	  var t = $(this).val();
	  var labelText = 'File : ' + t.substr(12, t.length);
	  $(this).prev('label').text(labelText);
	})
	
})
//jQuery time
		var nombre=document.getElementById("nombre").value;
		var apellidoPaterno=document.getElementById("apellidoPaterno").value;
		var apellidoMaterno=document.getElementById("apellidoMaterno").value;
		var sexo=document.getElementById("sexo").value;
		var fechaNacimiento=document.getElementById("fechaNacimiento").value;
		var direccion=document.getElementById("direccion").value;
		var colonia=document.getElementById("colonia").value;
		var codigoPostal=document.getElementById("codigoPostal").value;
		var estadoCivil=document.getElementById("estadoCivil").value;
		var escolaridad=document.getElementById("escolaridad").value;
		var especialidad=document.getElementById("especialidad").value;
		var curp=document.getElementById("curp").value;
		var nss=document.getElementById("nss").value;
		var idCiudad=document.getElementById("idCiudad").value;
		var idSucursal=document.getElementById("idSucursal").value;
		var idDepartamento=document.getElementById("idDepartamento").value;
		var idPuesto=document.getElementById("idPuesto").value;
		var fechaContratacion=document.getElementById("fechaContratacion").value;
		var tipo=document.getElementById("tipo").value;
		var idTurno=document.getElementById("idTurno").value;
		var salarioDiario=document.getElementById("salarioDiario").value;
		var diasVacaciones=document.getElementById("diasVacaciones").value;
		var diasPermiso=document.getElementById("diasPermiso").value;
		var email=document.getElementById("email").value;
		var password=document.getElementById("password").value;


var band=true;
function datoP()
{
	nombre=document.getElementById("nombre").value;
	apellidoPaterno=document.getElementById("apellidoPaterno").value;
	apellidoMaterno=document.getElementById("apellidoMaterno").value;
	sexo=document.getElementById("sexo").value;
	fechaNacimiento=document.getElementById("fechaNacimiento").value;
	direccion=document.getElementById("direccion").value;
	colonia=document.getElementById("colonia").value;
	codigoPostal=document.getElementById("codigoPostal").value;
	estadoCivil=document.getElementById("estadoCivil").value;

	if(nombre=="" || apellidoMaterno=="" || apellidoPaterno=="" || sexo=="" || fechaNacimiento=="" || direccion=="" || colonia=="" || codigoPostal=="" || estadoCivil=="")
	{
		band=false;
		console.log("falta nombre");
	} else{
		band=true;
		console.log("cambio");
	}
}
function datoPro()
{
	
	escolaridad=document.getElementById("escolaridad").value;
	especialidad=document.getElementById("especialidad").value;
	curp=document.getElementById("curp").value;
	nss=document.getElementById("nss").value;

	if(escolaridad=="" || especialidad=="" || curp=="" || nss=="" )
	{
		band=false;
		console.log("falta nombre");
	} else{
		band=true;
		console.log("cambio");
	}
}
function datoContra()
{
	
	idCiudad=document.getElementById("idCiudad").value;
	idSucursal=document.getElementById("idSucursal").value;
	idDepartamento=document.getElementById("idDepartamento").value;
	idPuesto=document.getElementById("idPuesto").value;
	fechaContratacion=document.getElementById("fechaContratacion").value;
	tipo=document.getElementById("tipo").value;
	idTurno=document.getElementById("idTurno").value;
	salarioDiario=document.getElementById("salarioDiario").value;
	diasVacaciones=document.getElementById("diasVacaciones").value;
	diasPermiso=document.getElementById("diasPermiso").value;
	if(idCiudad=="" || idSucursal=="" || idDepartamento=="" || idPuesto=="" || fechaContratacion=="" || tipo=="" || idTurno=="" || salarioDiario=="" || diasVacaciones=="" || diasPermiso=="")
	{
		band=false;
		console.log("falta nombre");
	} else{
		band=true;
		console.log("cambio");
	}
}
function datoSesion()
{
	
	var email=document.getElementById("email").value;
	var email=document.getElementById("password").value;

	if(email=="" || email==""  )
	{
		band=false;
		console.log("falta nombre");
	} else{
		band=true;
		console.log("cambio");
	}
}


$(document).ready(function(){

	

	var current_fs, next_fs, previous_fs; //fieldsets
	var opacity;
	var current = 1;
	var steps = $("fieldset").length;
	
	setProgressBar(current);
	
	$(".next").click(function(){
		
		//if(band){
			
		
		
		
			//
			current_fs = $(this).parent();
			next_fs = $(this).parent().next();
			
			//Add Class Active
			$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
			
			//show the next fieldset
			next_fs.show();
			//hide the current fieldset with style
			current_fs.animate({opacity: 0}, {
				step: function(now) {
					// for making fielset appear animation
					opacity = 1 - now;
					
					current_fs.css({
						'display': 'none',
						'position': 'relative'
					});
					next_fs.css({'opacity': opacity});
				},
				duration: 500
			});
			setProgressBar(++current);
		//}
	});
	
	$(".previous").click(function(){
	
		current_fs = $(this).parent();
		previous_fs = $(this).parent().prev();
		
		//Remove class active
		$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
		
		//show the previous fieldset
		previous_fs.show();
		
		//hide the current fieldset with style
		current_fs.animate({opacity: 0}, {
			step: function(now) {
			// for making fielset appear animation
			opacity = 1 - now;
			
				current_fs.css({
					'display': 'none',
					'position': 'relative'
				});
				previous_fs.css({'opacity': opacity});
			},
			duration: 500
		});
		setProgressBar(--current);
	});
	
	function setProgressBar(curStep){
		var percent = parseFloat(100 / steps) * curStep;
		percent = percent.toFixed();
		$(".progress-bar")
		.css("width",percent+"%")
	}
	
	$(".submit").click(function(){
		return false;
	})
	
});