(function(){
	
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


$(document).ready(function(){

	

	var current_fs, next_fs, previous_fs; //fieldsets
	var opacity;
	var current = 1;
	var steps = $("fieldset").length;
	
	setProgressBar(current);
	
	$(".next").click(function(){
		//
		if(nombre=="" || foto=="")
		
		{
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