let input1 = document.querySelector("#calculo1")
let input2 = document.querySelector("#calculo2")
let buttoncalcular = document.querySelector(".btnCalcular")
let h1 = document.querySelector("h1")
let result = document.querySelector(".result")
let formulario = document.querySelector("#formulario")
/*
console.log({
    h1,clase,id,input
})

h1.innerHTML = "html insertado <br> insertado";
h1.innerText = "texto sin html insertado"

clase.setAttribute('class', 'sobelo')
clase.classList.add('mirey')
clase.classList.remove('mirey')
input.value = "1234"

const img = document.createElement('img')
img.setAttribute('src', 'https://librosostenibilidad.files.wordpress.com/2017/03/paisaje-cultura-sostenibilidad.jpg?w=2000&h=1365&crop=1')
id.append(img)
*/

//buena práctica con addeventlistener en vez de onclick
buttoncalcular.addEventListener('click', sumarvalores)




function sumarvalores(e){
    e.preventDefault();
    result.innerText = "resultado es: " + (Number(input1.value) + Number(input2.value))
    console.log(Number(input1.value) + Number(input2.value))
}
