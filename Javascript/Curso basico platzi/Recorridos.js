var estudiantes = ["Sara", "María", "Sergio", "Daniel"]

function saludarEstudiantes(estudiante){
    console.log(`Hola, ${estudiante}`);
}
for(var estudiante of estudiantes){
    saludarEstudiantes(estudiante);
}
while (estudiantes.length > 0){
    var estudiante = estudiantes.shift();
    saludarEstudiantes(estudiante);
}