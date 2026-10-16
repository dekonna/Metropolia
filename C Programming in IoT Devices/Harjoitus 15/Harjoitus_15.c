#include <stdio.h>
#include <string.h>

#define MAX_ITEMS 40

typedef struct menu_item_ {
    char name[50];
    double price;
} menu_item;

int main(void) {
    char filename[100];
    menu_item menu[MAX_ITEMS];
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

    /* Luetaan tiedot taulukkoon (nimi ja hinta erotettu puolipisteellä) */
    // fscanf lukee merkkijonon ja desimaaliluvun %[^;] lukee kaiken ennen puolipistettä
    while (count < MAX_ITEMS && fscanf(file, " %49[^;];%lf", menu[count].name, &menu[count].price) == 2) {
        count++;
    }

    /* Suljetaan tiedosto */
    fclose(file);

    /* Tulostetaan taulukon sisältö muotoilluissa sarakkeissa */
    printf("\n--- MENU ---\n");
    for (int i = 0; i < count; i++) {
        // %8.2lf = hinta kahdella desimaalilla, varaa 8 merkkiä tilaa
        // %s = tuotteen nimi
        printf("%8.2lf  %s\n", menu[i].price, menu[i].name);
    }

    return 0;
}