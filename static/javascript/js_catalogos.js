  axios.defaults.xsrfCookieName = 'csrftoken'
  axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

function select_continente(id_primer_select, id_segundo_select){
    var primer_select = document.getElementById(id_primer_select);
    var segundo_select = document.getElementById(id_segundo_select);
    var alerta = document.getElementById('al-cat');
    alerta.style.display = "none";
    let req = axios ({
        method: 'POST',
        url: '/seleccion_continente/',
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFTOKEN',
        data : primer_select.value,
        headers : {
            'X-CSRFTOKEN':'csrftoken'
        }
    }).then((response)=>{
        this.msg = response.data;
        console.log(response.data);
        const htmlOptions = response.data
        .map(item => `<option value="${item}">${item}</option>`)
        .join('');
        console.log(htmlOptions);
        segundo_select.innerHTML = htmlOptions;
    });
    return;
}


function ocultar(id_btn_agr, id_btn_edit, id_btn_elim, id_primer_select, id_segundo_select, id_input){
    var bot_agr = document.getElementById(id_btn_agr); //Boton agregar
    var primer_select = document.getElementById(id_primer_select);
    var segundo_select = document.getElementById(id_segundo_select);
    var bot_edit = document.getElementById(id_btn_edit); //Boton editar
    var bot_elim = document.getElementById(id_btn_elim); //Boton eliminar
    var input = document.getElementById(id_input); //Input
    var alerta = document.getElementById('al-cat');
    alerta.style.display = "none";
    
    if(segundo_select.value !=segundo_select.options[0].value){
        //Si se quiere editar o eliminar:
        bot_agr.style.display = "none"; //Se bloquea el boton de agregar
        bot_edit.style.display = "inline"; //Se desbloquea el boton de editar
        bot_elim.style.display = "inline"; //Se desbloquea el boton de eliminar
        if(primer_select.value ==primer_select.options[0].value){
            valor = segundo_select.value
            guion = valor.indexOf('-') //Se identifica donde esta el guion
            primer_valor = valor.slice(0,guion)
            segundo_valor = valor.slice(guion+1) //Se extrae el segundo_valor de la variable 'valor'
            primer_select.value = segundo_valor //Se selecciona el segundo_valor correspondiente al país que ya había sido almacenado
            input.value = primer_valor;
        }else{
            input.value = segundo_select.value;
        }
        primer_select.disabled = true;
    }
    else{
        //Si se desea agregar:
        bot_agr.style.display = "inline"; //Se desbloquea el boton de agregar
        bot_edit.style.display = "none"; //Se bloquea el boton de editar
        bot_elim.style.display = "none";//Se bloquea el boton de eliminar
        // primer_select.value = primer_select.options[0].value;
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
    
    if(segundo_select.value !=segundo_select.options[0].value){
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
        primer_select.value = primer_select.options[0].value;
        input.value = ""; //Se deja en blanco el input
    }
}

function ocultar_per(id_btn_agr, id_btn_edit, id_btn_elim, id_primer_select, id_segundo_select, id_input1, id_input2, id_input3){
    var bot_agr = document.getElementById(id_btn_agr); //Boton agregar
    var primer_select = document.getElementById(id_primer_select);
    var segundo_select = document.getElementById(id_segundo_select);
    var bot_edit = document.getElementById(id_btn_edit); //Boton editar
    var bot_elim = document.getElementById(id_btn_elim); //Boton eliminar
    var input1 = document.getElementById(id_input1); //input1
    var input2 = document.getElementById(id_input2); //input1
    var input3 = document.getElementById(id_input3); //input1
    
    if(segundo_select.value !=segundo_select.options[0].value){
        //Si se quiere editar o eliminar:
        bot_agr.style.display = "none"; //Se bloquea el boton de agregar
        bot_edit.style.display = "inline"; //Se desbloquea el boton de editar
        bot_elim.style.display = "inline"; //Se desbloquea el boton de eliminar
        valor = segundo_select.value
        guion = valor.indexOf('-'); //Se identifica donde esta el guion
        mas = valor.indexOf('+'); //Se identifica donde esta el mas
        diagonal = valor.indexOf('/'); //Se identifica donde esta la diagonal
        primer_valor = valor.slice(0,guion);
        segundo_valor = valor.slice(guion+1,mas);
        tercer_valor=valor.slice(mas+1,diagonal);
        cuarto_valor=valor.slice(diagonal+1);
        input1.value = primer_valor;
        input2.value = segundo_valor;
        input3.value = tercer_valor;
        primer_select.value = cuarto_valor; //Se selecciona el segundo_valor correspondiente al país que ya había sido almacenado
    }
    else{
        //Si se desea agregar:
        bot_agr.style.display = "inline"; //Se desbloquea el boton de agregar
        bot_edit.style.display = "none"; //Se bloquea el boton de editar
        bot_elim.style.display = "none";//Se bloquea el boton de eliminar
        primer_select.value = primer_select.options[0].value;
        input1.value = ""; //Se deja en blanco el input
        input2.value = "";
        input3.value = "";
    }
}