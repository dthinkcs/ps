function changeBackgroundColor() {
    var colorInput = document.getElementById("colorInput").value;
    document.getElementById("box").style.background = colorInput;
}

var button = document.getElementById("submitColor");
button.addEventListener('click', changeBackgroundColor);



