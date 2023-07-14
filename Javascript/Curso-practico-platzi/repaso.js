//Convierte el siguiente código en una función, pero, cambiando cuando sea necesario las variables constantes por parámetros y argumentos en una función:
/*
const name = "Juan David";
const lastname = "Castro Gallego";
const completeName = name + lastname;
const nickname = "juandc";

console.log("Mi nombre es " + completeName + ", pero prefiero que me digas " + nickname + ".");
*/
function datos(name, lastname,nickname){
    this.name = name
    this.lastname = lastname
    this.nickname = nickname
    const completeName = name + lastname;
    console.log("Mi nombre es " + completeName + ", pero prefiero que me digas " + nickname + ".");
}

//condicionales
const tipoDeSuscripcion = "Basic";

if (tipoDeSuscripcion == "Free"){
    console.log("Solo puedes tomar los cursos gratis");
}else{
    tipoDeSuscripcion == "Basic" ? console.log("Puedes tomar casi todos los cursos de Platzi durante un mes"): tipoDeSuscripcion == "Expert" ? console.log("Puedes tomar casi todos los cursos de Platzi durante un año") : tipoDeSuscripcion == "ExpertPlus" ? console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año") : console.log("nada rey")
}
//otra manera sin usar condicionales y usando objetos/arrays y un solo condicional:

let tiposdesuscripciones = {
    free: "Solo puedes tomar los cursos gratis",
    basic: "Puedes tomar casi todos los cursos de Platzi durante un mes",
    Expert: "Puedes tomar casi todos los cursos de Platzi durante un año",
    ExpertPlus: "Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año"
}

function conseguirtipoSubscripcion(suscripcion){
    if (tiposdesuscripciones[suscripcion]){
        console.log(tiposdesuscripciones[suscripcion])
    }
}




//Replica el comportamiento de los siguientes ciclos for utilizando ciclos while:
/*
for (let i = 0; i < 5; i++) {
    console.log("El valor de i es: " + i);
}

for (let i = 10; i >= 2; i--) {
    console.log("El valor de i es: " + i);
}
*/
var i = 0
while (i<5){
    console.log("El valor de i es " + i);
    i++
}
var i = 10
while (i>=2){
    console.log("El valor de i es " + i);
    i--
}

//2️⃣ Crea una función que pueda recibir cualquier array como parámetro e imprima su primer elemento.
//3️⃣ Crea una función que pueda recibir cualquier array como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el array completo).
//4️⃣ Crea una función que pueda recibir cualquier objeto como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el objeto completo).
//2. 
var array = function(arreglo){
    return arreglo[0]
}
var imprimir = function(arreglo){
    for(let i=0; i<arreglo.length; i++){
        console.log(arreglo[i])
    }
}
//4
function readObject(object) {
    for (let key in object) {
      console.log(object.key);
    }
}
//otra manera
function imprimirunoporunoobjeto(objeto){
    const arreglo = Object.values(objeto) //va a almacenar en un arreglo los valores del objeto que se le pase
    for(let i = 0; i< arreglo.length; i++){
        console.log(arreglo[i])
    }
}