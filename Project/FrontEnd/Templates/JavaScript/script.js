
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

function cambiarTitulo() {
  const titulo = document.getElementById ("registro")
  titulo.innerHTML = "¡Bienvenido!"
}

function cambiarTituloOriginal() {
  const titulo2 = document.getElementById ("registro")
  titulo2.innerHTML = "Sé parte de esta comunidad"
}
  