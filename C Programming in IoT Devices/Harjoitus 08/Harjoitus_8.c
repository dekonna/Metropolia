#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Funktio tulostaa taulukon luvut omille riveilleen
   kahdeksan merkin levyisessä kentässä (%8d) */
void print_numbers(const int *array, int count) {
    int i;
    for (i = 0; i < count; i++) {
        printf("%8d\n", array[i]);
    }
}

int main(void) {
    int numbers[15];
    int i;

    /* Alustetaan satunnaislukugeneraattori */
    srand(time(NULL));

    /* Täytetään taulukko 15 satunnaisella kokonaisluvulla */
    for (i = 0; i < 15; i++) {
        numbers[i] = rand() % 100 + 1;
    }

    /* Kutsutaan funktiota taulukon tulostamiseksi */
    print_numbers(numbers, 15);

    return 0;
}