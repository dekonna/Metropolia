#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Valikko */
void print_menu(void) {
    printf("\n--- MENU ---\n");
    printf("1. Roll D6\n");
    printf("2. Roll D10\n");
    printf("3. Quit\n");
    printf("Select an operation: ");
}

/* Funktio hoitaa nopan heiton ja tulostaa satunnaisen tuloksen annetulta väliltä */
void roll_dice(int sides) {
    /* rand() % sides antaa luvun 0 ja (sides - 1) väliltä,
       siihen lisätään 1, jotta saadaan alue 1 - sides */
    int result = rand() % sides + 1;
    printf("You rolled D%d and got: %d\n", sides, result);
}

int main(void) {
    int choice;

    /* Alustetaan satunnaislukugeneraattori kerran ohjelman alussa */
    srand(time(NULL));

    /* Silmukka pitää valikon näkyvillä, kunnes käyttäjä valitsee 3 quit */
    while (1) {
        print_menu();

        /* Tarkistetaan, että käyttäjä syötti numeron */
        if (scanf("%d", &choice) == 1) {
            if (choice == 1) {
                roll_dice(6);
            }
            else if (choice == 2) {
                roll_dice(10);
            }
            else if (choice == 3) {
                printf("Quitting program. Bye!\n");
                break;
            }
            else {
                printf("Error: Invalid choice. Please select 1, 2, or 3.\n");
            }
        } else {
            printf("Error: Invalid input. Please enter a number.\n");
            /* Tyhjennetään virheellinen syöte puskurista, ettei jää ikuiseen silmukkaan */
            while (getchar() != '\n');
        }
    }

    return 0;
}