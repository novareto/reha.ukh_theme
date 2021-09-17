$(document).ready(function(){

    // Form Floating Labels
    $('input.form-control').on('focus blur', function (e) {
        var wrap = $(this).closest('.form-group');
        if (e.type == 'focus') {
            wrap.addClass('no-placeholder');
            return;
        }
        if ($(this).val()) {
            wrap.addClass('no-placeholder');
        }else{
            wrap.removeClass('no-placeholder');
        }
    });

});
