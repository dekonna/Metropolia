#ifndef TEMPERATURE_LOGIC_H
#define TEMPERATURE_LOGIC_H

#include "file_handler.h"

// Funktio, joka hakee annetun huoneen mittaukset ja tulostaa kaavion
void process_and_display_room(const TemperatureRecord records[], int total_records, const char *search_room);

#endif // TEMPERATURE_LOGIC_H