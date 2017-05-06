function sidebar() {
    $('.ui.labeled.icon.sidebar').sidebar('toggle');
}


$(document).ready(function() {
  $(document).on('keydown', function(e){
      (function() {

    var img = document.getElementById('container').firstChild;
    img.onload = function() {
        if(img.height > img.width) {
            img.height = '100%';
            img.width = 'auto';
        }
    };

    }());

  $('#doc_bar').on('click', function() {
    $.ajax({
      type: 'GET',
      url: '/history',
      success: function(data) {
        $('#sidebar').html(data);
      }
    });
  });

});
