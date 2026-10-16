#include <stdio.h>

/* Funktio kysyy ja tarkistaa onko luku annetulla välillä */
int read_range(int low, int high) {
    int number;

    while (1) {
        printf("Enter a number between %d and %d: ", low, high);

        /* Tarkistetaan, että syöte on onnistuneesti luettu kokonaisluku */
        if (scanf("%d", &number) == 1) {
            /* Tarkistetaan, että luku on määritellyllä välillä */
            if (number >= low && number <= high) {
                return number;
            } else {
                printf("Error: The number is not in the specified range.\n");
            }
        } else {
            printf("Invalid input. Please enter a valid integer.\n");
            /* Tyhjennetään virheellinen syöte pois puskurista */
            while (getchar() != '\n');
        }
    }
}

int main(void) {
    int round;
    int user_roll;

    printf("Let's play!\n");

    /* Pelataan peli läpi kolmen kierroksen ajan */
    for (round = 0; round < 3; round++) {
        printf("Roll a die and enter your result.\n");
        user_roll = read_range(1, 6);

        /* Ohjelma huijaa sääntöjen mukaan: jos käyttäjä saa 6, tulee tasapeli,
           muuten ohjelma ilmoittaa saaneensa aina yhden enemmän. */
        if (user_roll == 6) {
            printf("I got 6. It is a tie!\n");
        } else {
            printf("I got %d. I win!\n", user_roll + 1);
        }
    }

    printf("Better luck next time. Bye!\n");

    return 0;
}