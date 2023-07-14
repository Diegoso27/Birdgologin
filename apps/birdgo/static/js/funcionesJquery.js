
$(function(){
    $("#formaRegistro").validate({
        rules:{
            txtCorreo:{
                required: true,
                email: true
            },
            txtPassword:{
                required: true,
                minlength: 8              
                
            },
            txtPassword2:{  
                required: true,
                minlength: 8,
                equalTo: "#txtPassword"
            }
        },
        messages:{
            txtCorreo:{
                required:"Este campo es obligatorio",
                email: "El correo ingresado no es valido"
            },
            txtPassword:{
                required:"Este campo es obligatorio",
                minlength:"Debe contener al menos 8 caracteres"
            },
            txtPassword2:{
                required:"Este campo es obligatorio",
                minlength:"Debe contener al menos 8 caracteres",
                equalTo: "Las contraseñas no coinciden" 
            }
        }
    })
    $("#form-contacto").validate({
        rules:{ 
            txtCorreo: {
                required: true,
                email: true
            },
            pass1: {
                required: true,
                minlength: 8 
            },
            pass2: {
                required: true,
                minlength: 8,
                equalTo: "#pass1"
            },
            txtNombre: {
                required: true,
                minlength: 3
            },
            txtApellido: {
                required: true,
                minlength: 3
            },
            txtRut: {
                required: true,
                minlength: 9,
                number: true
            },
            txtAsunto: {
                required: true,
                minlength: 3
            },
            txtMensaje: {
                required: true
            }

        },
            messages:{
                txtCorreo:{
                    required:"Este campo es obligatorio",
                    email: "El correo ingresado no es valido"
                },
                pass1: {
                    required:"Este campo es obligatorio",
                    minlength:"Debe contener al menos 8 caracteres"
                },
                pass2: {
                    required:"Este campo es obligatorio",
                    minlength:"Debe contener al menos 8 caracteres",
                    equalTo: "Las contraseñas no coinciden" 
                },
                txtNombre: {
                    required:"Este campo es obligatorio",
                    minlength:"Debe contener al menos 3 caracteres"
                },
                txtApellido: {
                    required:"Este campo es obligatorio",
                    minlength:"Debe contener al menos 3 caracteres"
                },
                txtRut: {
                    required:"Este campo es obligatorio",
                    minlength:"Debe contener al menos 9 caracteres",
                    number: "El rut ingresado no es valido"
                },
                txtAsunto: {
                    required:"Este campo es obligatorio",
                    minlength:"Debe contener al menos 3 caracteres"
                },
                txtMensaje: {
                    required:"Por favor ingrese un mensaje"
                }

            }
    });
})
