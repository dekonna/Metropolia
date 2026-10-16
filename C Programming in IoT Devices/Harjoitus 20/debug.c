#include <stdio.h>
#include <stdarg.h>
#include "debug.h"

// Staattinen muuttuja, joka näkyy vain tämän tiedoston funktioille
static int current_debug_level = 0;

void set_debug_level(int debug_level) {
    current_debug_level = debug_level;
}

int dprint(int debug_level, const char *fmt, ...) {
    // Jos annettu debug level on pienempi tai yhtäsuuri kuin tallennettu taso
    if (debug_level <= current_debug_level) {
        fprintf(stderr, "[DBG%d] ", debug_level);

        va_list args;
        va_start(args, fmt);
        int result = vfprintf(stderr, fmt, args);
        va_end(args);

        return result;
    }

    // Muussa tapauksessa ei tulosteta mitään ja palautetaan nolla
    return 0;
}
