$(function(){
    $("#formaRegistro").validate({
        rules:{
            txtCorreo:{
                required: true,
                minlength:5
            },
            nombre:{
                required: true,
                minlength:5
            },
            apellido:{
                required: true,
                minlength:5
            },
            correo:{
                required:true,
                email:true
            }            
        },
        messages:{
            rut:{
                required:"Debe ingresar su rut",
                minlength:"Debe ingresar minimo 5 caracteres"
            },
            nombre:{
                required:"Debe ingresar su nombre",
                minlength:"Debe ingresar minimo 5 caracteres"
            },
            apellido:{
                required:"Debe ingresar su apellido",
                minlength:"Debe ingresar minimo 5 caracteres"
            },
            correo:{
                required:"Debe ingresar su correo",
                minlength:"Debe ingresar minimo 5 caracteres",
                email:"Correo no valido"
            },

            
        }
    })
})


$(function(){

})



$(document).ready(function(){
    $('#buscar').on('keyup', function(){
        let valor = $(this).val().toLowerCase();
        $('table tbody tr').filter(function(){
            $(this).toggle($(this).text().toLowerCase().indexOf(valor) > -1)
        })
    })
})



function apiJquery(){
    $.ajax({
        url:"https://mindicador.cl/api",
        dataType:"json",
        success: function(data){
            console.log(data);
            document.getElementById("dolar").innerHTML = "El valor del dolar es: " + data.dolar.valor;

        },
        error: function(error){
            console.error(error);
        }
    });
}