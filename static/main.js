function sidebar() {
    $('.ui.labeled.icon.sidebar').sidebar('toggle');
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

    $.ajax({
        type: 'POST',
        url: '/detect',
        data: $("#pic").attr('src'),
        contentType: 'text/plain',
        success: function(data) {
            console.log(data);
        }

    });



});
