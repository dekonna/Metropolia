/*
Harjoituksen pääasiat:
  - Käyttäjä syöte (scanf): bussi- ja taksihinnat sekä rahamäärä.
  - Toistorakenne (while): toistaa, kunnes rahat eivät enää riitä kumpaankaan.
  - Ehtolauseet (if-else): tarkistetaan rahojen riittävyys ja käyttäjän valinta (bussi/taksi).
  - Tilapäivitys: vähennetään hinta rahamäärästä ja tulostetaan jäljellä oleva saldo.
*/

#include <stdio.h>

int main() {
    float bus_price, taxi_price, money;
    int selection;

    printf("Enter price of bus ticket:  ");
    scanf("%f", &bus_price);

    printf("Enter price of taxi:  ");
    scanf("%f", &taxi_price);

    printf("How much money you have:  ");
    scanf("%f", &money);

    printf("You have %.2f euros left.\n", money);


    while (1) {
        if (money < bus_price && money < taxi_price) {
            printf("You need to walk. Bye\n");
            break;
        }

        printf("Do you want to take\n");
        printf("1) bus (%.2f euros)\n", bus_price);
        printf("2) taxi (%.2f euros)\n", taxi_price);
        printf("Enter your selection: ");
        scanf("%d", &selection);

        if (selection == 1) {
            printf("You chose bus.\n");
            if (money >= bus_price) {
                money -= bus_price;
                printf("You have %.2f euros left.\n", money);
            } else {
                printf("You don't have enough money for bus.\n");
                printf("You have %.2f euros left.\n", money);
            }

        } else if (selection == 2) {
            printf("You chose taxi.\n");
            if (money >= taxi_price) {
                money -= taxi_price;
                printf("You have %.2f euros left.\n", money);
            } else {
                printf("You don't have enough money for taxi.\n");
                printf("You have %.2f euros left.\n", money);
            }
        } else {
            printf("Invalid selection. Please choose 1 or 2.\n");
        }
    }

    return 0;
}