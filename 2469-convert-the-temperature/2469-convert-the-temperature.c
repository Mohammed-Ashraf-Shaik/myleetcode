#include <stdlib.h>

double* convertTemperature(double celsius, int* returnSize) {
    *returnSize = 2;

    double* result = (double*)malloc(2 * sizeof(double));
    if (result == NULL) return NULL; // check malloc success

    result[0] = celsius + 273.15;         // Kelvin
    result[1] = celsius * 1.80 + 32.00;   // Fahrenheit

    return result;
}
