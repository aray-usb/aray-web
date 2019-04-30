signUpButton = document.getElementById("signUp");
const signInButton = document.getElementById("signIn");
const container = document.getElementById("container");

signUpButton.addEventListener("click", () =>
container.classList.add("right-panel-active")
);

signInButton.addEventListener("click", () =>
container.classList.remove("right-panel-active")
);

// Configurations for the toastr, in wich a popup alert will be shown in the top rigth
// border of the screen in case of success or failure.
toastr.options = {
    "closeButton": true,
    "debug": false,
    "newestOnTop": false,
    "progressBar": false,
    "positionClass": "toast-top-right",
    "preventDuplicates": true,
    "showDuration": "300",
    "hideDuration": "1000",
    "timeOut": "5000",
    "extendedTimeOut": "1000",
    "showEasing": "swing",
    "hideEasing": "linear",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
}


function submitLoginForm() {
    console.log('yuuuuuuu');

    const $form = $('.login');
    const url = $form.attr('action');
    const method = $form.attr('method');
    const data = $form.serialize();
    console.log(data);
    console.log('aaaaaaaaaaaaaaaa');
    console.log($form);
/*     $.ajax({
        method: method,
        data: data,
        url: url,
        success: function(json) {
            const valid = json.valid,
            errors = json.errors.__all__
            // Verifica que no se presente errores 
            if (!valid) {
                // Si se presentan errores entonces se muestra un mensaje de error con el 
                // siguiente contenido
                toastr['error']('', 'Oferta con este Trimestre, Año y Coordinacion ya existe')
            } else {
                // Si no se presenta errores entonces se procede a mandar la informacion 
                // para que sea guardada 
                const $btn = $('#editar')
                const trimestre = $('#id_trimestre')
                const anio = $('#id_anio')
                const otrasAsignaturas = $('#todas-asignaturas')
                otrasAsignaturas.addClass('invisible')
                trimestre.attr('disabled', 'true')
                anio.attr('disabled', 'true')
                $('.tabla-asignaturas-oferta span').addClass('hide')
                $('#helper').addClass('d-none')
                $('#myInput').attr('onkeyup', 'myFunction()')
                $('#myInput').val('')
                $btn.find('span').removeClass('fa-save')
                $btn.find('span').addClass('fa-edit')
                toastr.success("Operación exitosa",'' )
                editable = !editable
            }


        }
    }) */
}


$(document).on('click', '#login-button', function() {
   
    submitLoginForm();
})