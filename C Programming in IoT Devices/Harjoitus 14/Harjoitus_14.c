#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_LINES 100
#define MAX_LENGTH 81  //  80 + 1

int main(void) {
    char filename[100];
    char lines[MAX_LINES][MAX_LENGTH];
    FILE *file;
    int count = 0;

    printf("Anna tiedoston nimi: ");
    if (fgets(filename, sizeof(filename), stdin) != NULL) {
        int len = strlen(filename);
        if (len > 0 && filename[len - 1] == '\n') {
            filename[len - 1] = '\0';
        }
    }

    /* Yritetään avata tiedosto lukemista varten */
    file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Virhe: Tiedoston '%s' avaaminen epaonnistui.\n", filename);
        return 1;
    }

    /* Luetaan rivit taulukkoon */
    while (count < MAX_LINES && fgets(lines[count], sizeof(lines[count]), file) != NULL) {
        count++;
    }

    /* Suljetaan tiedosto lukemisen jälkeen */
    fclose(file);

    /* Muutetaan kaikki kirjaimet isoiksi toupper funktiolla */
    for (int i = 0; i < count; i++) {
        for (int j = 0; lines[i][j] != '\0'; j++) {
            lines[i][j] = toupper((unsigned char)lines[i][j]);
        }
    }

    /* Avataan tiedosto uudelleen kirjoitusta varten "w" ja kirjoitetaan rivit takaisin */
    file = fopen(filename, "w");
    if (file == NULL) {
        fprintf(stderr, "Virhe: Tiedoston '%s' avaaminen kirjoitusta varten epaonnistui.\n", filename);
        return 1;
    }

    for (int i = 0; i < count; i++) {
        fputs(lines[i], file);
    }

    fclose(file);

    printf("Tiedosto kasitelty onnistuneesti! Kaikki kirjaimet muutettu isoiksi.\n");

    return 0;
}
