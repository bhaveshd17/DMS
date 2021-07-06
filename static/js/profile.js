let form_fields = document.getElementsByTagName('input')
let select_fields = document.getElementsByTagName('select')

for (let l of ["SE", "TE", "BE"].values()){
    document.getElementById('id_kt_'+l).classList = 'form-control'
    document.getElementById('id_drop_'+l).classList = 'form-control'

}
for (let field in select_fields) {
    select_fields[field].className += ' form-control'
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


let degree_select = document.getElementById("id_degree")
degree_select.addEventListener("change", (event)=>{
    let deploma_div = document.getElementById("diploma_div")
    if(event.target.value == 'diploma'){
        deploma_div.style.display = ""
    }
    else{
        deploma_div.style.display = "none"
    }
})

let input = document.getElementById( 'id_file' );
let label = document.getElementById( 'file-upload-label' );
input.addEventListener( 'change', showFileName );
function showFileName(event) {
  let input = event.srcElement;
  let fileName = input.files[0].name;
  if(fileName.length > 25){
    fileName = fileName.slice(0, 25) + '...'
  }
  label.textContent = 'file name: ' +fileName;
}