#include <stdio.h>
#include <string.h>
#include "file_handler.h"
#include "temperature_logic.h"
#include <stdlib.h>

#define MAX_RECORDS 100
#define FILENAME "Temperatures.csv"

int main(void) {
    system("chcp 65001 > nul"); // ääkköset
    TemperatureRecord records[MAX_RECORDS];

    // Luetaan tiedosto ohjelman alussa
    int total_records = read_temperature_file(FILENAME, records, MAX_RECORDS);

    if (total_records < 0) {
        printf("Ohjelman suoritus keskeytyy tiedoston virheen vuoksi.\n");
        return 1;
    }

    printf("Luettu onnistuneesti %d riviä tiedostosta '%s'.\n", total_records, FILENAME);

    char search_room[MAX_ROOM_NAME];

    // Pääsilmukka käyttäjien kyselyille
    while (1) {
        printf("\nSyötettävän huoneen nimi (tai kirjoita 'exit' poistuaksesi): ");

        // Luetaan käyttäjän syöte turvallisesti fgets-funktiolla
        if (fgets(search_room, sizeof(search_room), stdin) == NULL) {
            printf("Virhe syötteen lukemisessa.\n");
            break;
        }

        // Poistetaan mahdollinen rivinvaihto lopusta
        search_room[strcspn(search_room, "\r\n")] = 0;

        // Tarkistetaanko haluaako käyttäjä poistua
        if (strcasecmp(search_room, "exit") == 0 || strlen(search_room) == 0) {
            printf("Ohjelma suljetaan. Näkemiin!\n");
            break;
        }

        // Kutsutaan logiikkamoduulia huoneen etsimiseen ja tulostamiseen
        process_and_display_room(records, total_records, search_room);
    }

    return 0;
}