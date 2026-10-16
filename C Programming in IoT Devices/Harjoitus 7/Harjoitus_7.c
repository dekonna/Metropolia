#include <stdio.h>
#include <stdbool.h>

/* Funktio lukee positiivisen kokonaisluvun osoittimen kautta.
   Palauttaa true, jos syöte onnistui ja luku on positiivinen, muuten false. */
bool read_positive(int *value) {
    int temp;

    printf("Enter a positive number: ");

    /* Tarkistetaan, että scanf lukee onnistuneesti kokonaisluvun */
    if (scanf("%d", &temp) == 1) {
        /* Tarkistetaan, että luku on aidosti positiivinen (> 0) */
        if (temp > 0) {
            *value = temp; /* Tallennetaan arvo osoittimen kautta muistiin */
            return true;
        }
    } else {
        /* Jos lukeminen epäonnistui, tyhjennetään puskuri */
        while (getchar() != '\n');
    }

    return false;
}

int main(void) {
    int guess;
    int error_count = 0;

    /* Ohjelma pyörii, kunnes virheitä on tullut 3 kappaletta */
    while (error_count < 3) {
        printf("Guess how much money I have!\n");

        /* Kutsutaan funktiota ja tarkistetaan onnistuiko syöttö */
        if (read_positive(&guess)) {
            /* Lasketaan ohjelman salainen summa: kaksi kertaa arvaus plus 20 euroa */
            int correct_amount = guess * 2 + 20;
            printf("You didn't get it right. I have %d euros.\n", correct_amount);
        } else {
            /* Syöte epäonnistui tai luku ei ollut positiivinen */
            printf("Incorrect input\n");
            error_count++;
        }
    }

    printf("I give up! See you later!\n");

    return 0;
}