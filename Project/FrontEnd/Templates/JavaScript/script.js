
function validateForm() {
    let x = document.forms["myForm"]["username"].value;
    let y = document.forms["myForm"]["password"].value;
    if (x == "") {
      alert("Debe ingresar un usuario");
      return false;
    }
    if (y == "") {
        alert("Debe ingresar una contraseña");
        return false;
      }

  }
  