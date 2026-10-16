#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "file_handler.h"


int read_temperature_file(const char *filename, TemperatureRecord records[], int max_records) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Virhe: Tiedostoa '%s' ei voitu avata.\n", filename);
        return -1;
    }

    char line[MAX_LINE_LENGTH];
    int count = 0;
    int line_number = 0;

    // Luetaan tiedosto rivi riviltä
    while (fgets(line, sizeof(line), file) != NULL) {
        line_number++;

        // Poistetaan mahdollinen rivinvaihto lopusta
        line[strcspn(line, "\r\n")] = 0;

        // Tarkistetaan onko rivi tyhjä
        if (strlen(line) == 0) {
            continue; // Ohitetaan tyhjät rivit
        }

        // Ohitetaan ensimmäinen otsikkorivi (esim. "Temperature, Room" tai "Room, Temperature")
        if (line_number == 1 && (strstr(line, "Temperature") || strstr(line, "Room"))) {
            continue;
        }

        // Tarkistetaan, että rivi ei ole liian pitkä (jos puuttuu loppumerkki, rivi saattaa olla katkennut)
        // fgets lukee enintään sizeof(line)-1 merkkiä. Jos viimeinen merkki ei ole '\0' tai rivinvaihto, se oli liian pitkä.

        // Pilkotaan rivi pilkun kohdalta (formaatti voi olla: "22.5, Kitchen" tai "Kitchen, 22.5")
        // Katsotaan kummin päin tiedosto on muotoiltu. Temperatures.csv:ssä on "Temperature, Room" tai toisinpäin.
        // Puretaan turvallisesti strtok-funktiolla:
        char *token1 = strtok(line, ",");
        char *token2 = strtok(NULL, ",");

        if (token1 == NULL || token2 == NULL) {
            printf("Varoitus: Virheellinen rivi %d tiedostossa (ohitetaan).\n", line_number);
            continue;
        }

        // Poistetaan mahdolliset ylimääräiset välilyönnit merkkijonojen alusta/lopusta
        
        // Selvitetään kumpi on luku ja kumpi huoneen nimi
        float temp = 0.0f;
        char room_name[MAX_ROOM_NAME];

        // Tarkistetaan kummassa tokenissa on numerotietoa
        if (sscanf(token1, "%f", &temp) == 1) {
            // token1 oli lämpötila, token2 on huone
            sscanf(token2, " %[^\t\n]", room_name); // Otetaan huoneen nimi mukaan lukien välilyönnit (esim. "Living Room")
        } else if (sscanf(token2, "%f", &temp) == 1) {
            // token1 oli huone, token2 oli lämpötila
            sscanf(token1, " %[^\t\n]", room_name);
        } else {
            printf("Varoitus: Riviä %d ei voitu jäsentää (ohitetaan).\n", line_number);
            continue;
        }

        // Tallennetaan taulukkoon, jos tilaa on
        if (count < max_records) {
            records[count].temperature = temp;
            // Poistetaan mahdolliset johtavat/jälkimmäiset välilyönnit huoneen nimestä
            // (Yksinkertainen kopiointi)
            char *start = room_name;
            while(*start == ' ') start++;
            
            snprintf(records[count].room, sizeof(records[count].room), "%s", start);
            count++;
        } else {
            printf("Varoitus: Tiedostossa on enemmän rivejä kuin varattu muisti sallii (%d).\n", max_records);
            break;
        }
    }

    fclose(file);
    return count;
}