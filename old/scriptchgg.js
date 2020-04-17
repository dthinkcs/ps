// get the element summonModal and remove the class hide from it to show it
document.getElementById("summonModal").addEventListener('click', function() {
    document.getElementById("modal").classList.remove("hide");
});

// get the element closeModal and add the class hide to it to hide it
document.getElementById("closeModal").addEventListener('click', function() {
    document.getElementById("modal").classList.add("hide");
});
