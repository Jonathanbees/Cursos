/*
Palabras reservadas y conversión de tipos de datos(casting)
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(){
    int a = 5;
    float b = 3.14;
    char c = 'A';
    bool d = false;
    printf("El valor de a es: %d\n", a);
    printf("El valor de b es: %f\n", b);
    printf("El valor de c es: %c\n", c);
    printf("El valor de d es: %d\n", d);
    printf("El valor de d es: %s\n", d ? "true" : "false");
    //Recorridos de arreglos
    int tamaño;
    printf("Ingrese el tamaño del arreglo: ");
    scanf("%i", &tamaño);

// Allocate memory for the array
    int* arreglo = (int*)calloc(tamaño,sizeof(int));

    if (arreglo == NULL) {
        printf("Memory allocation failed.\n");
        return 1; // or handle error as appropriate
    }

    for(int i = 0; i < tamaño; i++){
        printf("Ingrese el valor del elemento %d: ", i+1);
        scanf("%d", &arreglo[i]);
    }
    printf("Los valores del arreglo son: ");
    for(int i = 0; i < tamaño; i++){
        printf("%d ", arreglo[i]);
    }

printf("\n");

// Don't forget to free the memory when you're done with it
free(arreglo);

}