#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_ITEMS 40

typedef struct menu_item_ {
    char name[50];
    double price;
} menu_item;

// Vertaifunktio nimen mukaan järjestämistä varten
int compare_by_name(const void *a, const void *b) {
    const menu_item *item1 = (const menu_item *)a;
    const menu_item *item2 = (const menu_item *)b;
    return strcmp(item1->name, item2->name);
}

// Vertaifunktio hinnan mukaan järjestämistä varten
int compare_by_price(const void *a, const void *b) {
    const menu_item *item1 = (const menu_item *)a;
    const menu_item *item2 = (const menu_item *)b;
    if (item1->price < item2->price) return -1;
    if (item1->price > item2->price) return 1;
    return 0;
}

int main(void) {
    char filename[100];
    menu_item menu[MAX_ITEMS];
    FILE *file;
    int count = 0;

    // Kysytään tiedoston nimi käyttajältä
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

    // Luetaan tiedot taulukkoon
    while (count < MAX_ITEMS && fscanf(file, " %49[^;];%lf", menu[count].name, &menu[count].price) == 2) {
        count++;
    }

    // Suljetaan tiedosto
    fclose(file);

    if (count == 0) {
        printf("Ei tuotteita tiedostossa tai lukeminen epaonnistui.\n");
        return 0;
    }

    // Kysytään kayttäjältä järjestysvalintaa
    int choice;
    printf("Valitse jarjestys (1 = hinnan mukaan, 2 = nimen mukaan): ");
    if (scanf("%d", &choice) != 1) {
        printf("Virheellinen syote.\n");
        return 1;
    }

    // Järjestetään taulukko qsortin avulla
    if (choice == 1) {
        qsort(menu, count, sizeof(menu_item), compare_by_price);
    } else {
        qsort(menu, count, sizeof(menu_item), compare_by_name);
    }

    // Tulostetaan järjestetty menu
    printf("\n--- MENU ---\n");
    for (int i = 0; i < count; i++) {
        printf("%8.2lf  %s\n", menu[i].price, menu[i].name);
    }

    return 0;
}
