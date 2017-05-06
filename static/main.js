function sidebar() {
    $('.ui.labeled.icon.sidebar').sidebar('toggle');
}

function findSleep() {

    $.ajax({
        type: 'POST',
        url: '/detect',
        data: $("#pic").attr('src'),
        contentType: 'text/plain',
        success: function(data) {
            $("#sleep").html("睡觉学生： ");
            $("#sleep").show();
            for(var i=0; i<data['id'].length; i++)
                $("#sleep").append(data['id'][i]);
        }
    });
}


$(document).ready(function() {
    (function() {
    var img = document.getElementById('container').firstChild;
    img.onload = function() {
        if(img.height > img.width) {
            img.height = '100%';
            img.width = 'auto';
        }

    };
    }());


});
