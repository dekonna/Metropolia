#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int find_first(const unsigned int *array, unsigned int what) {
    int i = 0;

    /* Käydään taulukkoa läpi, kunnes vastaan tulee nolla */
    while (array[i] != 0) {
        if (array[i] == what) {
            return i; // Palauttaa indeksin, josta luku löytyi
        }
        i++;
    }

    return -1; // Jos lukua ei löytynyt ennen nollaa
}

int main(void) {
    unsigned int numbers[20];
    int i;
    unsigned int etsittava;

    /* Alustetaan satunnaislukugeneraattori */
    srand(time(NULL));

    /* Täytetään 19 ensimmäistä alkiota luvuilla 1-20 */
    for (i = 0; i < 19; i++) {
        numbers[i] = (rand() % 20) + 1;
    }

    /* Asetetaan viimeinen alkio nollaksi (lopetusmerkki) */
    numbers[19] = 0;

    /* Tulostetaan taulukon sisällöt yksi luku per rivi */
    printf("Taulukon luvut:\n");
    for (i = 0; i < 20; i++) {
        printf("%u\n", numbers[i]);
    }
    printf("\n");

    /* Kysytään käyttäjältä lukuja, kunnes annetaan nolla */
    while (1) {
        printf("Anna etsittava luku (0 lopettaa): ");
        scanf("%u", &etsittava);

        if (etsittava == 0) {
            break;
        }

        int tulos = find_first(numbers, etsittava);

        if (tulos != -1) {
            printf("Loytyi indeksista %d\n", tulos);
        } else {
            printf("not found\n");
        }
    }

    return 0;
}