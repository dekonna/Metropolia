#ifndef FILE_HANDLER_H
#define FILE_HANDLER_H

#define MAX_LINE_LENGTH 256
#define MAX_ROOM_NAME 64

// Tietorakenne yksittäiselle lämpötilamittaukselle
typedef struct {
    char room[MAX_ROOM_NAME];
    float temperature;
} TemperatureRecord;

// Funktio, joka lukee tiedoston ja tallentaa tulokset taulukkoon.
// Palauttaa luettujen rivien määrän.
int read_temperature_file(const char *filename, TemperatureRecord records[], int max_records);

#endif // FILE_HANDLER_H

