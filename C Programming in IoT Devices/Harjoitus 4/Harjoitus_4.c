#include <stdio.h>

/* Funktio lukee kokonaisluvun käyttäjältä. Jos syöte on virheellinen,
   tulostetaan "invalid input" ja yritetään uudelleen. */
int read_integer(void) {
    int number;

    while (1) {
        printf("Enter positive numbers or negative to stop: ");

        /* Tarkistetaan, että scanf lukee onnistuneesti kokonaisluvun */
        if (scanf("%d", &number) == 1) {
            return number;
        } else {
            printf("invalid input\n");

            /* Tyhjennetään virheellinen syöte pois puskurista */
            while (getchar() != '\n');
        }
    }
}

int main(void) {
    int count = 0;
    int sum = 0;
    int current_number;

    while (1) {
        current_number = read_integer();

        /* Jos luku on negatiivinen, lopetetaan silmukka */
        if (current_number < 0) {
            break;
        }

        sum = sum + current_number;
        count = count + 1;
    }

    /* Lasketaan ja tulostetaan keskiarvo kolmen deseminaalin tarkkuudella,
       jos lukuja on syötetty vähintään yksi */
    if (count > 0) {
        double average = (double)sum / count;
        printf("You entered %d positive numbers. The average is: %.3f\n", count, average);
    } else {
        printf("You entered 0 positive numbers.\n");
    }

    return 0;
}