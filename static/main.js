function sidebar() {
    $('.ui.labeled.icon.sidebar').sidebar('toggle');
}
function analyzeRecord() {

    $.ajax({
        type: 'POST',
        url: '/analyze',
        data: $("#pic").attr('src'),
        contentType: 'text/plain',
        success: function(data) {
            if(data['flag'] == '1'){
                $("#record").html(data['analyze_result']);
                $("#record").show();
                $("#sleep").html("睡觉学生： ");
                $("#sleep").show();
                for(var i=0; i<data['id'].length; i++)
                    $("#sleep").append(data['id'][i]);
            }
            else{
                $("#record").html(data['analyze_result']);
                $("#record").show();
            }

        }
    });
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
            if(data['id'].length == 0){
                $("#sleep").append("None");
            }
            for(var i=0; i<data['id'].length; i++)
                $("#sleep").append(data['id'][i]);
        }
    });
}

function capturePhoto() {

    $.ajax({
        type: 'POST',
        url: '/capture',
        success: function(data) {
            new_url = data['new_url'];
            $("#pic").attr('src', new_url);
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
