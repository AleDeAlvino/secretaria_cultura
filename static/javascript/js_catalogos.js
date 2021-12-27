function ocultar(id_btn_agr, id_s_p_c, id_s_c_c, id_btn_edit, id_btn_elim, id_inp_pais){
    var bot_agr = document.getElementById(id_btn_agr); //Boton agregar
    var se_pais = document.getElementById(id_s_p_c); //Select país
    var se_continente = document.getElementById(id_s_c_c); //Select continente
    var bot_edit = document.getElementById(id_btn_edit); //Boton editar
    var bot_elim = document.getElementById(id_btn_elim); //Boton eliminar
    var input_pais = document.getElementById(id_inp_pais); //Input país
    
    if(se_pais.value != 'Selecciona un país para editar'){ //Se verifica si selecciono un pais para editar
        //Si se quiere editar o eliminar:
        bot_agr.style.display = "none"; //Se bloquea el boton de agregar
        bot_edit.style.display = "inline"; //Se desbloquea el boton de editar
        bot_elim.style.display = "inline"; //Se desbloquea el boton de eliminar
        valor = se_pais.value //Se extrae la información del pais seleccionado
        guion = valor.indexOf('-') //Se identifica donde esta el guion
        pais = valor.slice(0,guion) //Se extrae el pais de la variable 'valor'
        continente = valor.slice(guion+1) //Se extrae el continente de la variable 'valor'
        input_pais.value = pais // Al input se le da el valor del país
        se_continente.value = continente //Se selecciona el continente correspondiente al país que ya había sido almacenado
    }
    else{
        //Si se desea agregar:
        bot_agr.style.display = "inline"; //Se desbloquea el boton de agregar
        bot_edit.style.display = "none"; //Se bloquea el boton de editar
        bot_elim.style.display = "none";//Se bloquea el boton de eliminar
        input_pais.value = ""; //Se deja en blanco el input
    }
}