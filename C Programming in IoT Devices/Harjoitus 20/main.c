#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "debug.h"

int main(void) {
    srand(time(NULL));
    int user_level;

    printf("Anna debug-taso (0-4): ");
    if (scanf("%d", &user_level) != 1) {
        printf("Virheellinen syote.\n");
        return 1;
    }

    // Asetetaan debug level
    set_debug_level(user_level);

    // Tulostetaan viisi viestiä satunnaisella debug levelillä (0-4)
    for (int i = 1; i <= 5; i++) {
        int random_level = rand() % 5; // Arpoo luvun 0-4
        dprint(random_level, "Tassa on viesti numero %d\n", i);
    }

    return 0;
}