#include <stdio.h>
#include <string.h>

int replace_char(char *str, const char *repl) {
    int i = 0;
    int count = 0;

    /* Tarkistetaan, että korvaavassa merkkijonossa on tasan kaksi merkkiä */
    if (repl[0] == '\0' || repl[1] == '\0' || repl[2] != '\0') {
        return 0;
    }

    char etsittava = repl[0];
    char korvaava = repl[1];

    /* Käydään merkkijono läpi merkki kerrallaan */
    while (str[i] != '\0') {
        if (str[i] == etsittava) {
            str[i] = korvaava;
            count++;
        }
        i++;
    }

    return count;
}

int main(void) {
    char text[100];
    char repl[10];

    printf("Anna muokattava merkkijono: ");
    if (fgets(text, sizeof(text), stdin) != NULL) {
        int pituus = strlen(text);
        if (pituus > 0 && text[pituus - 1] == '\n') {
            text[pituus - 1] = '\0';
        }
    }

    printf("Anna kaksi merkkia (esim. e3): ");
    if (fgets(repl, sizeof(repl), stdin) != NULL) {
        int pituus = strlen(repl);
        if (pituus > 0 && repl[pituus - 1] == '\n') {
            repl[pituus - 1] = '\0';
        }
    }

    /* Kutsutaan funktiota */
    int tulos = replace_char(text, repl);

    /* Tulostetaan tulos */
    if (tulos > 0) {
        printf("Korvauksien maara: %d\n", tulos);
        printf("Muokattu merkkijono: %s\n", text);
    } else {
        printf("String was not modified\n");
    }

    return 0;
}