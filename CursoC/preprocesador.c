#include <stdio.h>
#include <stdlib.h>
#define PI 3.1416 // Macro para definir el valor de PI
#define CUBO(x) x*x*x // Macro para calcular el cubo de un número

int main(){
    float suma;
    suma = PI + 3;
    printf("La suma es: %f\n", suma);
    printf("El cubo de 3 es: %d\n", CUBO(3));
    return 0;
}