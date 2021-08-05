function validatePan() {
    var pan_no = document.getElementById("id_pan_card_no").value;
    var regex = /([A-Z]){5}([0-9]){4}([A-Z]){1}$/;
    var regex1 = /([A-Z]){3}([0-9]){6}([A-Z]){1}$/;
    if (regex.test(pan_no.toUpperCase()) || regex1.test(pan_no.toUpperCase())) {
        document.getElementById("pan_error").style.display = 'none'
    } else {
        document.getElementById("pan_error").style.display = ''
    }
}

function validatePassport() {
    var patt = new RegExp("^([A-Z a-z]){1}([0-9]){7}$")
    var pass_no = document.getElementById("id_passport_no").value;
    if (patt.test(pass_no)) {
        document.getElementById("pass_error").style.display = 'none'
    }
    else {
        document.getElementById("pass_error").style.display = ''
    }
}

$(document).ready(function() {
    $("#id_pan_card_no").change(function() {
        validatePan()
    });
    $("#id_passport_no").change(function() {
        validatePassport()
    });
});