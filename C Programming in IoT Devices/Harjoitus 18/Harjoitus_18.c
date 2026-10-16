#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    // Alustetaan satunnaislukugeneraattori
    srand(time(NULL));

    int input;

    while (1) {
        printf("Anna luku (0-15) tai negatiivinen luku lopettaaksesi: ");
        if (scanf("%d", &input) != 1) {
            break;
        }

        // Jos luku on negatiivinen, ohjelma pysähtyy
        if (input < 0) {
            break;
        }

        // Tarkistetaan, että luku on annetulla välillä
        if (input > 15) {
            printf("Virhe: Luvun taytyy olla valilta 0-15!\n");
            continue;
        }

        // Generoidaan satunnaisluku
        int rand_num = rand();

        // Tulostetaan arvottu luku heksadesimaalina
        printf("Arvottu luku hex: %X\n", rand_num);

        // Siirretään lukua oikealle käyttäjän antaman määrän verran
        int shifted = rand_num >> input;

        // // Rajataan luku niin, että vain 6 alimmaista bittiä jää jäljelle
        int result = shifted & 0x3F;

        // Tulostetaan tulos heksadesimaalina, jossa on vähintään kaksi numeroa ja etunollat esim 03,04,05
        printf("Tulos hex: %02X\n\n", result);
    }

    return 0;
}