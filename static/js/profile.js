let form_fields = document.getElementsByTagName('input')
document.getElementById('id_degree').classList = 'form-control';
document.getElementById('id_roll_no').value = '{{request.user}}'
document.getElementById('id_rollNo').value = '{{request.user}}'
for (let i = 1; i <= 4; i++) {
    document.getElementById('id_roll_no_' + String(i)).value = '{{request.user}}'
}
for (let field in form_fields) {
    form_fields[field].className += ' form-control'
}
document.getElementById('id_percentage').type = 'text';
document.getElementById('id_start_year').type = 'date';
document.getElementById('id_start_date').type = 'date';
document.getElementById('id_end_year').type = 'date';



let details_cards = document.getElementById("details_cards")
window.addEventListener("resize", function () {
    if (window.innerWidth < 982) {
        details_cards.classList.remove("w-50")
    }
    else {
        details_cards.classList.add("w-50")
    }
});
if (window.innerWidth < 982) {
    details_cards.classList.remove("w-50")
}