#include <stdio.h>
#include <string.h>

int main(void) {
    char filename[100];
    FILE *file;
    int number;
    int count = 0;
    int lowest = 0;
    int highest = 0;


    printf("Anna tiedoston nimi: ");
    if (fgets(filename, sizeof(filename), stdin) != NULL) {
        int len = strlen(filename);
        if (len > 0 && filename[len - 1] == '\n') {
            filename[len - 1] = '\0';
        }
    }

    /* Avataan tiedosto suoraan annetulla nimellä */
    file = fopen(filename, "r");

    /* Jos avaaminen epäonnistuu, ilmoitetaan virheestä */
    if (file == NULL) {
        fprintf(stderr, "Virhe: Tiedoston '%s' avaaminen epaonnistui.\n", filename);
        return 1;
    }

    /* Luetaan luvut tiedostosta */
    while (fscanf(file, "%d", &number) == 1) {
        if (count == 0) {
            lowest = number;
            highest = number;
        } else {
            if (number < lowest) {
                lowest = number;
            }
            if (number > highest) {
                highest = number;
            }
        }
        count++;
    }

    /* Suljetaan tiedosto */
    fclose(file);

    /* Tulostetaan tulokset */
    if (count > 0) {
        printf("Luettujen lukujen maara: %d\n", count);
        printf("Pienin luku: %d\n", lowest);
        printf("Suurin luku: %d\n", highest);
    } else {
        printf("Tiedosto oli tyhja tai sielta ei loytynyt lukuja.\n");
    }

    return 0;
}