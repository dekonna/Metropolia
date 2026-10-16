#include <stdio.h>
#include <string.h>

int count_words(const char* str, const char *word) {
    int count = 0;
    const char *p = str;
    int pituus = strlen(word);

    /* Jos etsittävä sana on tyhjä, palautetaan 0 */
    if (pituus == 0) {
        return 0;
    }

    /* Etsitään samankaltaisuuksia silmukassa */
    while ((p = strstr(p, word)) != NULL) {
        count++;
        p += pituus;
    }

    return count;
}

int main(void) {
    char merkkijono[100];
    char sana[50];

    while (1) {
        printf("Anna merkkijono: ");
        if (fgets(merkkijono, sizeof(merkkijono), stdin) == NULL) {
            break;
        }

        int len = strlen(merkkijono);
        if (len > 0 && merkkijono[len - 1] == '\n') {
            merkkijono[len - 1] = '\0';
        }

        printf("Anna etsittava sana: ");
        if (fgets(sana, sizeof(sana), stdin) == NULL) {
            break;
        }

        len = strlen(sana);
        if (len > 0 && sana[len - 1] == '\n') {
            sana[len - 1] = '\0';
        }

        /* Jos sana on "stop", ohjelma pysähtyy */
        if (strcmp(sana, "stop") == 0) {
            break;
        }

        /* Kutsutaan funktiota ja tulostetaan paluuarvo */
        int tulos = count_words(merkkijono, sana);
        printf("Esiintymien maara: %d\n\n", tulos);
    }

    return 0;
}