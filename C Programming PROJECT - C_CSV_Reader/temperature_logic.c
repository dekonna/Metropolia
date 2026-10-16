#include <stdio.h>
#include <string.h>
#include "temperature_logic.h"

void process_and_display_room(const TemperatureRecord records[], int total_records, const char *search_room) {
    int found = 0;

    printf("\nLämpötilat huoneelle: %s\n", search_room);
    printf("----------------------------------------\n");

    for (int i = 0; i < total_records; i++) {
        // Vertaillaan huoneen nimeä (case-insensitive tai suora vertailu)
        if (strcasecmp(records[i].room, search_room) == 0) {
            found = 1;
            float temp = records[i].temperature;

            // Tulostetaan lämpötila yhden desimaalin tarkkuudella
            printf("%5.1f °C | ", temp);

            // Tarkistetaan onko lämpötila sallitulla alueella (0 - 30)
            if (temp < 0.0f || temp > 30.0f) {
                printf("X (Virheellinen alue)\n");
            } else {
                // Yksi viiva (-) jokaista 0.5 astetta kohti
                int dash_count = (int)(temp / 0.5f);
                for (int j = 0; j < dash_count; j++) {
                    printf("-");
                }
                printf("\n");
            }
        }
    }

    if (!found) {
        printf("Virhe: Huonetta '%s' ei löytynyt tiedostosta.\n", search_room);
    }
    printf("----------------------------------------\n");
}