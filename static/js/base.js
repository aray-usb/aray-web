const orgIdContainer = '#org-container'

/**
 * Mostrar el modal para mostrar la informacion de la asignatura
 * @param agregar booleano que dice si es un modal para agregar una nueva asignatura
 */
function show_informacion_modal(agregar){
    $('#agregar-modal').modal();

    $('.delete-form input').attr('type', 'button');

    console.log('agregar', agregar)
    if (!agregar) {
        console.log("proeans")
        $('#submit-btn').addClass('d-none');
        $('.asignatura-btn').removeClass('d-none');
        $('.editar_asignatura').html('<i class="far fa-edit"></i>');
        $('.editar_asignatura').addClass('btn-success');
        $('.editar_asignatura').removeClass('btn-primary');

        $('#eliminar-btn').attr('data-codasig', $('[name="detail_codasig"]').val())
        $('.editar_asignatura').attr('data-id', $('[name="detail_id"]').val())
    }
    else {
        // activarPlugins()
        $('#submit-btn').removeClass('d-none');
        $('.asignatura-btn').addClass('d-none');
    }
}

/**
 * Obtener del backend información de la asignatura cuando
 * se abre el modal para editar.
 * @param btn botón presionado
 * @param url url a donde hacer el GET request
 * @param agregar booleano que dice si es un modal para agregar
 */
function obtenerOrganizacion(btn, url, agregar) {
    $.ajax({
        url: url,
        method: 'GET',
        success: (form) => {
            console.log(form)
            $(orgIdContainer).html(form);
            // $('#info-pan').tab('show')
            show_informacion_modal(agregar);
            edit_mode = false;
        },
        error: (err) => {
            console.log(err)
        }
    })
}