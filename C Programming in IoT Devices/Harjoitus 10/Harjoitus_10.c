#include <stdio.h>
#include <string.h>

int main(void) {
    char merkkijono[100];

    while (1) {
        printf("Anna merkkijono: ");

        /* Luetaan syöte fgets-funktiolla */
        if (fgets(merkkijono, sizeof(merkkijono), stdin) == NULL) {
            break;
        }

        /* Poistetaan rivinvaihto merkkijonon lopusta */
        int pituus = strlen(merkkijono);
        if (pituus > 0 && merkkijono[pituus - 1] == '\n') {
            merkkijono[pituus - 1] = '\0';
            pituus--; // Päivitetään pituus ilman rivinvaihtoa
        }

        /* Tulostetaan merkkijonon pituus */
        printf("Pituus: %d\n", pituus);

        /* Tarkistetaanko onko syöte stop */
        if (strcmp(merkkijono, "stop") == 0) {
            break; // Lopetetaan ohjelma
        }
    }

    return 0;
}