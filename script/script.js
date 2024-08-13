// script.js

// Funktion zum Öffnen des Modals und Anzeigen des angeklickten Bildes
function openModal(imgElement) {
    var modal = document.getElementById("myModal");
    var modalImg = document.getElementById("modalImg");
  
    modal.style.display = "block";
    modalImg.src = imgElement.src;
  }
  
  // Funktion zum Schließen des Modals
  var closeBtns = document.getElementsByClassName("close");
  for (var i = 0; i < closeBtns.length; i++) {
    closeBtns[i].addEventListener("click", function() {
      var modal = this.parentElement;
      modal.style.display = "none";
    });
  }
  
