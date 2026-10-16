#include <stdio.h>
#include <stdlib.h>

int main() {
    int num_students;

    printf("How many students: ");
    scanf("%d", &num_students);

    int *grades = (int *)malloc(num_students * sizeof(int));
    if (grades == NULL) {
        return 1;
    }

    for (int i = 0; i < num_students; i++) {
        grades[i] = -1;
    }

    int student_num;

    while (1) {
        printf("Enter student number (1 - %d) or 0 to stop: ", num_students);
        scanf("%d", &student_num);

        if (student_num == 0) {
            break;
        }

        if (student_num < 1 || student_num > num_students) {
            printf("Invalid student number!\n");
            continue;
        }

        int grade;

        while (1) {
            printf("Enter grade (0 - 5) for student %d or -1 to cancel: ", student_num);
            scanf("%d", &grade);

            if ((grade >= 0 && grade <= 5) || grade == -1) {
                break;
            }
            printf("Invalid grade!\n");
        }

        grades[student_num - 1] = grade;
    }

    printf("\nStudent   Grade\n");
    for (int i = 0; i < num_students; i++) {
        if (grades[i] == -1) {
            printf("%-9d N/A\n", i + 1);
        } else {
            printf("%-9d %d\n", i + 1, grades[i]);
        }
    }

    free(grades);

    return 0;
}