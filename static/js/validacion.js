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