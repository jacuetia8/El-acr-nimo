$(function(){

    $('#buscar').keyup(function() {
    
        $.ajax({
            type: "POST",
            url: "/home/buscar/",
            data: { 
                'buscar' : $('#buscar').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
        
    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#resultados-busqueda').html(data);
}