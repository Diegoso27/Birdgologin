

//* RELOJ *//

function mostrarHora() {
    let date = new Date();
    let hora = date.getHours();
    let minuto = date.getMinutes();
    let segundo = date.getSeconds();
    let dia = date.getDay();
    let mes = date.getMonth();
    let ano = date.getFullYear();
    let dia_semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
    let hora_actual  = hora + ":" + minuto + ":" + segundo;
    document.write("Hora actual: " + hora_actual);
    
    

}