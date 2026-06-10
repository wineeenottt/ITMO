#include <stdio.h>
#include "ui.h"

void runApp() {
    MeteorologicalLog log;
    initLog(&log);

    int choice;
    while (1) {
        printf("\nМеню:\n");
        printf("1. Добавить новую запись\n");
        printf("2. Удалить запись по дате\n");
        printf("3. Показать записи по месяцу\n");
        printf("4. Выход\n");
        printf("> ");
        if (scanf("%d", &choice) != 1) {
            printf("Ошибка\n");
            break;
        }

        if (choice == 1) {
            MeteorologicalRecord rec;
            printf("Введите дату (dd mm yyyy): ");
            scanf("%d %d %d", &rec.day, &rec.month, &rec.year);
            printf("Температура: ");
            scanf("%lf", &rec.temperature);
            printf("Давление: ");
            scanf("%lf", &rec.pressure);
            printf("Осадки (дождь/снег/ничего): ");
            scanf("%s", rec.precipitation);
            addRecord(&log, rec);
        } else if (choice == 2) {
            int d, m, y;
            printf("Введите дату для удаления записи (dd mm yyyy): ");
            scanf("%d %d %d", &d, &m, &y);
            deleteByDate(&log, d, m, y);
        } else if (choice == 3) {
            int m, y;
            printf("Введите месяц (mm yyyy): ");
            scanf("%d %d", &m, &y);
            showByMonth(&log, m, y);
        } else if (choice == 4) {
            printf("Выход...\n");
            break;
        } else {
            printf("Ошибка\n");
        }
    }

    freeLog(&log);
}
