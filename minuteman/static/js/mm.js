$(function(){
    $('.oneliner').click(function(e){
        $('#time').addClass('green');
    });


    $('.start').click(function(e){
        console.log(e);
        var project_id = $('#id_project').val();
        var text_stuff = $('#text').val();
        $.post('/start/', {project:project_id, comments:text_stuff}, function(data){
            $('.start').addClass('started').removeClass('start');
            $('.tableheader').after('<tr class=hiddenFirst><td>' + project_id + '</td><td>'+ project_id +'</td><td>0</td><td>' + text_stuff + '</td><td id=topRight></td></tr>');
            $('#newproject').toggle();
            $('.oneliner').toggle();
            $('.stop').appendTo( $('#topRight') );
            $('input[name="project"]').val(project_id);
            $('#finish').toggle();

        });
        return false;
    });

    $('.stop').click(function(e){
        var project_id = $('#id_project').val();
        $.post('/stop/', {project:project_id}, function(data){

            $('#finish').toggle();
            $('.hiddenFirst').toggle();
            $('#newproject').toggle();
            $('.oneliner').toggle();

        });
        return false
    });

    $('.continue').click(function(e){

    });
});