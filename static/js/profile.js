let form_fields = document.getElementsByTagName('input')
let select_fields = document.getElementsByTagName('select')

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
let profile_info = document.getElementById("profile_info")
window.addEventListener("resize", function () {
    if (window.innerWidth < 982) {
        details_cards.classList.remove("w-75")
        profile_info.classList.remove("w-75")

    }
    else {
        details_cards.classList.add("w-75")
        profile_info.classList.add("w-75")
    }
});
if (window.innerWidth < 982) {
    details_cards.classList.remove("w-75")
    profile_info.classList.remove("w-75")
}


let degree_select = document.getElementById("id_degree")
degree_select.addEventListener("change", (event)=>{
    let diploma_div = document.getElementById("diploma_div")
    if(event.target.value === 'diploma'){
        diploma_div.style.display = ""
        document.getElementById("no_of_sub").style.display = "none"
        document.getElementById("id_diploma_pattern").value = ""
        document.getElementById("id_diploma_aggregate_mw").value = ""
        document.getElementById("id_diploma_aggregate_pw").value = ""
        document.getElementById("id_no_of_dead_kt").value = ""
    }
    else{
        diploma_div.style.display = "none"
        document.getElementById("no_of_sub").style.display = ""
        document.getElementById("id_diploma_pattern").value = "NA"
        document.getElementById("id_diploma_aggregate_mw").value = "NA"
        document.getElementById("id_diploma_aggregate_pw").value = "NA"
        document.getElementById("id_no_of_dead_kt").value = "NA"
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




function curr_edu(input){
    for(let i =1; i<=4; i++) {
        if(i == input){
            document.getElementById(String(i)).style.display = ""
        }
        else{
            document.getElementById(String(i)).style.display = "none"
        }   
    }
    for(let i=1; i<=8;i++){
        let n=0;
        if(input == 1) n = 1;
        else if(input == 2) n = 3;
        else if (input == 3) n = 5;
        else if(input == 4) n= 7;
        if(i == n || i == n+1){
            document.getElementById("id_sgpi"+String(i)).value = ""
        }
        else{
            document.getElementById("id_sgpi"+String(i)).value = "NA"
        }
    }
    for(let i=1; i<=4; i++){
        if(i == input){
            document.getElementById("id_cgpa"+String(i)).value = ""
        }
        else{
            document.getElementById("id_cgpa"+String(i)).value = "NA"
        }
        
    }
}

let eng_year = document.getElementById("year")
eng_year.addEventListener('change', (event)=>{
    let input = event.target.value;
    if(input === "1") curr_edu(Number(1))
    if(input === "2") curr_edu(Number(2))
    if(input === "3") curr_edu(Number(3))
    if(input === "4") curr_edu(Number(4))
})

