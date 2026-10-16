#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

// Funktio, joka luo salasanan
bool generate_password(char *dest, int size, const char *word) {
    int word_len = strlen(word);
    int needed_size = word_len * 2 + 1;

    // Tarkistetaan, mahtuuko salasana taulukkoon
    if (needed_size >= size) {
        return false;
    }

    int dest_index = 0;
    int word_index = 0;

    // Generoidaan salasana merkki kerrallaan
    for (int i = 0; i < needed_size; i++) {
        if (i % 2 == 0) {
            // Parilliset indeksit, satunnainen tulostettava merkki valilta 33-126
            char rand_char = (char)(33 + (rand() % 94));
            dest[dest_index] = rand_char;
        } else {
            // Joka toinen merkki on kirjain sanasta
            dest[dest_index] = word[word_index];
            word_index++;
        }
        dest_index++;
    }

    // Lisataan null merkkijonon loppuun
    dest[dest_index] = '\0';

    return true;
}

int main(void) {
    // Alustetaan satunnaislukugeneraattori
    srand(time(NULL));

    char word[32]; // Koko 32
    char password[100];

    while (1) {
        printf("Anna sana (tai 'stop'): ");
        if (scanf("%31s", word) != 1) {
            break;
        }

        // Tarkistetaan lopetuskomento
        if (strcmp(word, "stop") == 0) {
            break;
        }

        // Kutsutaan funktiota ja tulostetaan tulos tai virhe
        if (generate_password(password, sizeof(password), word)) {
            printf("Salasana: %s\n", password);
        } else {
            printf("Virhe: Sana on liian pitka!\n");
        }
    }

    return 0;
}