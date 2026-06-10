#include <stdio.h>
#include "domain.h"

void printRecord(const MeteorologicalRecord* r) {
    printf("Дата: %02d.%02d.%d\n", r->day, r->month, r->year);
    printf("Температура: %.1f C\n", r->temperature);
    printf("Давление: %.1f hPa\n", r->pressure);
    printf("Осадки: %s\n", r->precipitation);
}
