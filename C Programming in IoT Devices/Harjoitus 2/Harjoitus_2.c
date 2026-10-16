#include <stdio.h>

int main() {
    float salaries[12];
    float taxes[12];
    float tax_rate, income_limit, higher_tax_rate;
    float total_income = 0.0f;

    printf("Enter tax rate: ");
    scanf("%f", &tax_rate);

    printf("Enter income limit: ");
    scanf("%f", &income_limit);

    printf("Enter tax rate for income over the limit: ");
    scanf("%f", &higher_tax_rate);

    for (int i = 0; i < 12; i++) {
        printf("Enter income for month %d: ", i + 1);
        scanf("%f", &salaries[i]);
    }

    for (int i = 0; i < 12; i++) {
        float salary = salaries[i];
        float tax = 0.0f;

        if (total_income >= income_limit) {
            tax = salary * (higher_tax_rate / 100.0f);
        } else if (total_income + salary > income_limit) {
            float income_below_limit = income_limit - total_income;
            float income_above_limit = (total_income + salary) - income_limit;

            tax = (income_below_limit * (tax_rate / 100.0f)) +
                  (income_above_limit * (higher_tax_rate / 100.0f));
        } else {
            tax = salary * (tax_rate / 100.0f);
        }

        taxes[i] = tax;
        total_income += salary;
    }

    printf("\n");
    printf("%-5s %10s %10s\n", "month", "income", "tax");

    for (int i = 0; i < 12; i++) {
        printf("%-5d %10.2f %10.2f\n", i + 1, salaries[i], taxes[i]);
    }

    return 0;
}