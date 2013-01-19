$(function(){
    $('.oneliner').click(function(e){
        $('#time').addClass('green');
    });


    $('.start').click(function(e){
        console.log(e);
        var project_id = $('#id_project').val();
        var text_stuff = $('#text').val();
        var finish = $('#finish');
        console.log(finish);
        $.post('/start/', {project:project_id, comments:text_stuff}, function(data){
            $('.start').addClass('started').removeClass('start');
            $('.tableheader').after('<tr><td>' + project_id + '</td><td>'+ project_id +'</td><td>0</td><td>' + text_stuff + '</td><td class="farRight"><form action="/start/" method="post" class="start">' +
                '<input type="hidden" value=' + project_id + ' name="project"><button class="continue" type="submit" name="action" value="resume">'+
                'Continue on this</button></form></td></tr>');
            $('#newproject').toggle();
            $('.oneliner').toggle();
            $('.stop').appendTo( $('.farRight') );
            $('input[name="project"]').val(project_id);
            $('#finish').first().val(project_id).toggle();
            $('.rows').last().remove();
            $('.continue').first().toggle();
        });
        return false;
    });

    $('.stop').click(function(e){
        var project_id = $('input[name="project"]').val();
        $.post('/stop/', {project:project_id}, function(data){
            $('.continue').first().toggle();
            $('#finish').toggle();
            $('#newproject').toggle();
            $('.oneliner').toggle();
            $('#id_project').val('');
            $('#text').val('');
        });
        return false
    });

//    $('.continue').click(function(e){
//
//    });
});