function consultarEstado(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/estado/nombre/"+nombre;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}


function consultarEmail(){
    var ajax=new XMLHttpRequest();
    var email=document.getElementById("email").value;
    var url="/empleados/correo/"+email;
    var div=document.getElementById("NotiEmail");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}



function consultarEmpleadoCurp(){
    var ajax=new XMLHttpRequest();
    var curp=document.getElementById("curp").value;
    var url="/empleados/curp/"+curp;
    var div=document.getElementById("NotiCurp");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                console.log("si entro")
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                console.log("no entro")
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}



function consultarEmpleadoNSS(){
    var ajax=new XMLHttpRequest();
    var nss=document.getElementById("nss").value;
    var url="/empleados/nss/"+nss;
    var div=document.getElementById("NotiNSS");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                console.log("si entro")
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                console.log("no entro")
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}



function consultarSalarioPuest(){
    var ajax=new XMLHttpRequest();
    var salarioDiario=document.getElementById("salarioDiario").value;
    var idPuesto=document.getElementById("idPuesto").value;
    var url="/empledo/salario/"+salarioDiario+","+idPuesto;
    var div=document.getElementById("salarioNoti");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                console.log("es igual")
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                console.log("no es igual")
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}




function consultarDocumento(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombreDocumento").value;
    var idEmpleado=document.getElementById("idEmpleado").value;
    var url="/documento/nombre/"+nombre+","+idEmpleado;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                console.log("es igual")
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                console.log("no es igual")
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarSucuNom(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/sucursales/nombre/"+nombre;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}


function conValidSal(){
    var ajax=new XMLHttpRequest();
    var fechaInicio=document.getElementById("salarioMinimo").value;
    var fechaFin=document.getElementById("salarioMaximo").value;

    //display:none; 

    if(fechaFin<fechaInicio)
    {
        
        let textoe="Salario Maximo incorrecto";
        
        document.getElementById("notifioMM").innerText=textoe;
        document.getElementById("registrar").setAttribute("disabled","true");
        document.getElementById("notifioMM").style.display = "block";
    }else{
        
        document.getElementById("registrar").removeAttribute("disabled");
        document.getElementById("notifioMM").style.display = "none";
    }
}

function datoSesion()
{

	var email=document.getElementById("email").value;
	var pass=document.getElementById("password").value;
	var banderaNum=false;
	var banderaMy=false;
	var banderaE=false;

	for(i=0; i<pass.length;i++)
	{
		var codigo = pass.charCodeAt(i);
		if(codigo>=48 && codigo<=57)
		{
			banderaNum= true;
		}
		if(codigo>=65 && codigo<=90)
		{
			banderaMy= true;
		}
		if((codigo>=32 && codigo<=47) || (codigo>=58 && codigo<=64) || (codigo>=91 && codigo<=96)|| (codigo>=123 && codigo<=126))
		{
			banderaE= true;
		}
	}


}

function horaTuno(){
    var ajax=new XMLHttpRequest();
    var fechaInicio=document.getElementById("horaInicio").value;
    var fechaFin=document.getElementById("horaFin").value;

    //display:none; 

    if(fechaFin<fechaInicio)
    {
        
        let textoe="Horario no valido";
        
        document.getElementById("notifcTurn").innerText=textoe;
        document.getElementById("registrar").setAttribute("disabled","true");
        document.getElementById("notifcTurn").style.display = "block";
    }else{
        
        document.getElementById("registrar").removeAttribute("disabled");
        document.getElementById("notifcTurn").style.display = "none";
    }
}




function consultarPfechas(){
    var ajax=new XMLHttpRequest();
    var fechaInicio=document.getElementById("fechaInicio").value;
    var fechaFin=document.getElementById("fechaFin").value;
    
    var url="/fechas/"+fechaInicio+","+fechaFin;
    var div=document.getElementById("notificacionesFechaMM");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                console.log("es igual")
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                console.log("no es igual")
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarSucuTel(){
    var ajax=new XMLHttpRequest();
    var telefono=document.getElementById("telefono").value;
    var url="/sucursales/telefono/"+telefono;
    var div=document.getElementById("notificacionesTel");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarEstadoSig(){
    var ajax=new XMLHttpRequest();
    var siglas=document.getElementById("siglas").value;
    var url="/estadoSig/siglas/"+siglas;
    var div=document.getElementById("notificacionesSig");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function vnombre(){
    
      
    var nombre=document.getElementById("nombre1").value;
    if(nombre=="")
    {
        console.log("hola")
        document.getElementById("next").setAttribute("disabled","true");
    }else{
        document.getElementById("next").removeAttribute("disabled");
    }

}

function consultarCiudad(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/ciudad/nombre/"+nombre;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarDepartamento(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/departamento/nombre/"+nombre;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarPuesto(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/puesto/nombre/"+nombre;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarTurno(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/turno/nombre/"+nombre;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarPercepcion(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/percepcion/nombre/"+nombre;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarDeduccion(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/deduccion/nombre/"+nombre;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarPeriodo(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/periodo/nombre/"+nombre;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarFormaPago(){
    var ajax=new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/formaPago/nombre/"+nombre;
    var div=document.getElementById("notificacionesNom");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}
function validarSalario(){
    
    var ajax=new XMLHttpRequest();
    var fechaInicio=document.getElementById("salarioMinimo").value;
    var fechaFin=document.getElementById("salarioMaximo").value;

    //display:none; 

    if(fechaFin<fechaInicio)
    {
        
        let texto="El salario de ingresado es incorrect";
        
        document.getElementById("notificacionesSalarioMM").innerText.texto;
        
        document.getElementById("notificacionesSalarioMM").style.display = "block";
        document.getElementById("registrar").setAttribute("disabled","true");
    }else{
        
        
        document.getElementById("notificacionesSalarioMM").style.display = "none";
        document.getElementById("registrar").removeAttribute("disabled");
    }
}

function passwordRobusto(pwd){
    var banNumero=false,banMin=false,banMay=false,banCarEs=false;
    banNumero=tieneNumero(pwd);
    banMin=tieneLetraMinuscula(pwd);
    banMay=tieneLetraMayuscula(pwd);
    banCarEs=tieneCaracterEspecial(pwd);
    if(banNumero && banMin && banMay && banCarEs)
        return '';
    else
        return 'El password debe tener al menos un digito,<br> una mayuscula, una minuscula y al menos un caracter especial.<br>'
}

function llenarSucursales(){
    var ajax = new XMLHttpRequest();
    ciudad = document.getElementById("idCiudad");
    select = document.getElementById("idSucursal");
    for(i = 0; i<=select.options.length;i++){
      select.remove(0);
    }
    var url = "/sucursalesCiudad/" + ciudad.value;
    ajax.open("get", url, true);
    ajax.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        var respuesta=JSON.parse(this.responseText);
        for(var i in respuesta){
          option = document.createElement("option");
          option.value = respuesta[i].id;
          option.text = respuesta[i].nombre;
          select.appendChild(option);
        }

      }
    };
    ajax.send();

  }

function llenarCiudades(){
    var ajax = new XMLHttpRequest();
    estado = document.getElementById("idEstado");
    select = document.getElementById("idCiudad");
    for(i = 0; i<=select.options.length;i++){
      select.remove(0);
    }
    var url = "/ciudadesEstado/" + estado.value;
    ajax.open("get", url, true);
    ajax.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        var respuesta=JSON.parse(this.responseText);
        for(var i in respuesta){
          option = document.createElement("option");
          option.value = respuesta[i].id;
          option.text = respuesta[i].nombre;
          select.appendChild(option);
        }

      }
    };
    ajax.send();

  }
