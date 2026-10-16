#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    int number;
    struct node *next;
} nnode;

int main(void) {
    char input[100];
    nnode *head = NULL;  // Osoittaa listan ensimmäiseen solmuun
    nnode *tail = NULL;  // Osoittaa listan viimeiseen solmuun

    printf("Anna lukuja (kirjoita 'end' lopettaaksesi):\n");

    while (1) {
        printf("Anna kokonaisluku: ");
        if (scanf("%99s", input) != 1) {
            break;
        }

        // Tarkistetaanko lopetuskomento
        if (strcmp(input, "end") == 0) {
            break;
        }

        // Tarkistetaan onko syöte kelvollinen kokonaisluku
        int num;
        char extra;
        // sscanf tarkistaa, että koko syöte on pelkkä luku
        if (sscanf(input, "%d %c", &num, &extra) == 1) {
            // Luodaan uusi solmu dynaamisesti muistiin
            nnode *new_node = (nnode *)malloc(sizeof(nnode));
            if (new_node == NULL) {
                fprintf(stderr, "Virhe: Muistin varaus epaonnistui!\n");
                break;
            }

            new_node->number = num;
            new_node->next = NULL;

            // Liitetään solmu listaan
            if (head == NULL) {
                // Ensimmäinen solmu
                head = new_node;
                tail = new_node;
            } else {
                // Lisätään listan perään
                tail->next = new_node;
                tail = new_node;
            }
        } else {
            // Virheellinen syöte
            printf("Virhe: Syota kokonaisluku tai 'end'.\n");
        }
    }

    // Tulostetaan kaikki syötetyt luvut
    printf("\nSyotetyt luvut listassa:\n");
    nnode *current = head;
    while (current != NULL) {
        printf("%d\n", current->number);
        current = current->next;
    }

    // Vapautetaan dynaamisesti varattu muisti
    current = head;
    while (current != NULL) {
        nnode *temp = current;
        current = current->next;
        free(temp);
    }

    return 0;
}