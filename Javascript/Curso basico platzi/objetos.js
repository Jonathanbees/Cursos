var carros = []
var cantidadregistrados = 0

function auto(marca, modelo, año){
    this.marca = marca
    this.modelo = modelo
    this.año = año
}

/*
var carro2 = new auto("tesla", "x", 2023)
var carro3 = new auto("hyundai", "nosé rey", 2021)
var carro4 = new auto("huawei", "otra cosa", 2022)
*/

var cantidadconstruir = prompt("Cuantos carros desea agregar?")
while(cantidadregistrados < cantidadconstruir){
    let marca = prompt("Marca: ")
    let modelo = prompt("modelo: ")
    let año = prompt("año: ")
    var carro = new auto(marca, modelo, año)

    carros.push(carro)
    cantidadregistrados++
}
//filtrado que obtiene los objetos que tengan el año igual a lo que uno quiera (2020)
var autosFiltrados = carros.filter(function(auto){
    return auto.año == 2020;
});

//mapeado que obtiene los valores del parámetro que se mande, para este caso, marca
var marcasRecientes = listaAutos.map(function(auto){
    return auto.marca;
});
//recorrer cada carro por el parámetro que se quiera y retornarlo
carros.forEach(function(auto){
    console.log(auto.modelo)
})
//filtrado que obtiene EL PRIMER OBJETO que tengan el año igual a lo que uno quiera (2020)
var autosFiltrados = carros.find(function(auto){
    return auto.año == 2020;
});




/*
var miAuto = {
    marca: "Toyota",
    modelo: "Corolla",
    año: 2020,
    detalleDelauto: function(){
        console.log(`Auto ${this.modelo}, ${this.año}`);
    }
}
miAuto.detalleDelauto();
*/