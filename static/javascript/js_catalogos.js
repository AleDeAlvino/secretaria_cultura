function ocultar(id_btn_agr, id_btn_edit, id_btn_elim, id_primer_select, id_segundo_select, id_input){
    var bot_agr = document.getElementById(id_btn_agr); //Boton agregar
    var primer_select = document.getElementById(id_primer_select); //Select continente
    var segundo_select = document.getElementById(id_segundo_select); //Select país
    var bot_edit = document.getElementById(id_btn_edit); //Boton editar
    var bot_elim = document.getElementById(id_btn_elim); //Boton eliminar
    var input = document.getElementById(id_input); //Input país
    
    if(segundo_select.value !=segundo_select.options[0].value){ //Se verifica si selecciono un pais para editar
        //Si se quiere editar o eliminar:
        bot_agr.style.display = "none"; //Se bloquea el boton de agregar
        bot_edit.style.display = "inline"; //Se desbloquea el boton de editar
        bot_elim.style.display = "inline"; //Se desbloquea el boton de eliminar
        valor = segundo_select.value //Se extrae la información del pais seleccionado
        guion = valor.indexOf('-') //Se identifica donde esta el guion
        pais = valor.slice(0,guion) //Se extrae el pais de la variable 'valor'
        continente = valor.slice(guion+1) //Se extrae el continente de la variable 'valor'
        input.value = pais // Al input se le da el valor del país
        primer_select.value = continente //Se selecciona el continente correspondiente al país que ya había sido almacenado
    }
    else{
        //Si se desea agregar:
        bot_agr.style.display = "inline"; //Se desbloquea el boton de agregar
        bot_edit.style.display = "none"; //Se bloquea el boton de editar
        bot_elim.style.display = "none";//Se bloquea el boton de eliminar
        input.value = ""; //Se deja en blanco el input
    }
}

function ocultar_dep(id_btn_agr, id_btn_edit, id_btn_elim, id_primer_select, id_segundo_select, id_input, id_check_uno, id_check_dos){
    var bot_agr = document.getElementById(id_btn_agr); //Boton agregar
    var primer_select = document.getElementById(id_primer_select); 
    var segundo_select = document.getElementById(id_segundo_select); 
    var bot_edit = document.getElementById(id_btn_edit); //Boton editar
    var bot_elim = document.getElementById(id_btn_elim); //Boton eliminar
    var input = document.getElementById(id_input); //Input
    
    if(segundo_select.value !=segundo_select.options[0].value){ //Se verifica si selecciono un pais para editar
        //Si se quiere editar o eliminar:
        bot_agr.style.display = "none"; //Se bloquea el boton de agregar
        bot_edit.style.display = "inline"; //Se desbloquea el boton de editar
        bot_elim.style.display = "inline"; //Se desbloquea el boton de eliminar
        valor = segundo_select.value
        guion = valor.indexOf('-') //Se identifica donde esta el guion
        mas = valor.indexOf('+')
        dependencia = valor.slice(0,guion) //Se extrae la dependencia de la variable 'valor'
        pais = valor.slice(guion+1,mas) //Se extrae el pais de la variable 'valor'
        pertenencia = valor.slice(mas+1)
        if (pertenencia == 'True'){
            document.getElementById(id_check_uno).checked=true;
        }
        else{
            document.getElementById(id_check_dos).checked=true;
        }
        input.value = dependencia // Al input se le da el valor del dependencia
        primer_select.value = pais //Se selecciona el pais correspondiente al país que ya había sido almacenado
    }
    else{
        //Si se desea agregar:
        bot_agr.style.display = "inline"; //Se desbloquea el boton de agregar
        bot_edit.style.display = "none"; //Se bloquea el boton de editar
        bot_elim.style.display = "none";//Se bloquea el boton de eliminar
        input.value = ""; //Se deja en blanco el input
    }
}