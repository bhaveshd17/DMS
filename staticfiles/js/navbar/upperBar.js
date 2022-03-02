let menu = document.getElementById('menu-btn')
window.addEventListener("resize", function () {
if (window.innerWidth < 991) {
    menu.style.display = ""
}
else {
    menu.style.display = "none"
}
});
if (window.innerWidth < 991) {
menu.style.display = ""
}
