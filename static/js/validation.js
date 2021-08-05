function validatePan() {
    var pan_no = document.getElementById("id_pan_card_no").value;
    var regex = /([A-Z]){5}([0-9]){4}([A-Z]){1}$/;
    var regex1 = /([A-Z]){3}([0-9]){6}([A-Z]){1}$/;
    if (regex.test(pan_no.toUpperCase()) || regex1.test(pan_no.toUpperCase())) {
        document.getElementById("pan_error").style.display = 'none'
        return true
    } else {
        document.getElementById("pan_error").style.display = ''
        return false
    }
}

function validatePassport() {
    var patt = new RegExp("^([A-Z a-z]){1}([0-9]){7}$")
    var pass_no = document.getElementById("id_passport_no").value;
    if (patt.test(pass_no)) {
        document.getElementById("pass_error").style.display = 'none'
        return true
    }
    else {
        document.getElementById("pass_error").style.display = ''
        return false
    }
}

$("input").addClass("form-control")
$("textarea").addClass("form-control")
$("select").addClass("form-control")
$("#id_date_of_birth").prop('type', 'date')

$(document).ready(function () {
    $("#id_pan_card_no").change(function() {
        validatePan()
    });
    $("#id_passport_no").change(function() {
        validatePassport()
    });
    $("#next1").click(function () {
        let roll_no = $("#id_roll_no").val()
        let pass1 = $("#id_password1").val()
        let pass2 = $("#id_password2").val()
        if (pass1 === pass2 && pass1.length >= 8) {
            $("#id_username").val(roll_no)
            $("#first").hide()
            $("#third").hide()
            $("#second").show()
        } else {
            alert("Password didn't match with Conform Password")
            $("#id_small").text("password should be same and must be greater than 8 characters.")
        }


    })
    $("#next2").click(function () {
        if(!validatePan()){
            alert("Enter valid pan card number")
        }
        else if(!validatePassport()){
            alert("Enter Valid Passport Number")
        }
        else{
            $("#first").hide()
            $("#second").hide()
            $("#third").show()
        }
    })

})
function showPassword() {
    let x = $("#id_password1")
    if (x.attr('type') === "password") {
        x.attr('type', 'text');
    } else {
        x.attr('type', 'password');
    }
}
function showCPassword(){
    let x = $("#id_password2")
    if (x.attr('type') === "password") {
        x.attr('type', 'text');
    } else {
        x.attr('type', 'password');
    }
}

let disability_d = document.getElementById("id_disability")
disability_d.addEventListener("change", (event)=>{
    let div = document.getElementById("disability_block")
    if(event.target.value === "true"){
        div.style.display = ""
        document.getElementById("id_type_of_disability").value = ""
    }
    else {
        div.style.display = "none"
        document.getElementById("id_type_of_disability").value = "NA"
    }
})