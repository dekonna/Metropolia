#include <stdio.h>
#include <string.h>

#define MAX_LINE 256

int main(void) {
    char filename[100];
    char line[MAX_LINE];
    FILE *file;

    // Kysytaan tiedoston nimi käyttäjältä
    printf("Anna tiedoston nimi: ");
    if (fgets(filename, sizeof(filename), stdin) != NULL) {
        int len = strlen(filename);
        if (len > 0 && filename[len - 1] == '\n') {
            filename[len - 1] = '\0';
        }
    }

    // Avataan tiedosto lukemista varten
    file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Virhe: Tiedoston '%s' avaaminen epaonnistui.\n", filename);
        return 1;
    }

    // Luetaan tiedostoa rivi rivilta
    while (fgets(line, sizeof(line), file) != NULL) {
        // Etsitaan dollarin merkki ja täysi / tähti
        char *start = strchr(line, '$');
        char *asterisk = strchr(line, '*');

        // Jos molemmat löytyvät ja täysi on dollarin jälkeen
        if (start != NULL && asterisk != NULL && asterisk > start) {
            unsigned char calculated_checksum = 0;

            // Lasketaan XOR (0/1) kaikkien merkkien välissä ($ ja *)
            for (char *p = start + 1; p < asterisk; p++) {
                calculated_checksum ^= (unsigned char)*p;
            }

            // Luetaan tähden jälkeen tuleva heksadesimaalinen checksum arvo
            unsigned int file_checksum = 0;
            if (sscanf(asterisk + 1, "%2x", &file_checksum) == 1) {
                // Verrataan laskettua ja tiedostosta luettua arvoa
                if (calculated_checksum == (unsigned char)file_checksum) {
                    printf("[ OK ] %s", line);
                } else {
                    printf("[ FAIL ] %s", line);
                }
            } else {
                // Jos heksalukua ei löydy oikeassa muodossa
                printf("[ FAIL ] %s", line);
            }
        }
    }

    // Suljetaan tiedosto
    fclose(file);
    return 0;
}