#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "collection.h"

void initLog(MeteorologicalLog* log) {
    log->size = 0;
    log->capacity = 10;
    log->records = (MeteorologicalRecord*)malloc(log->capacity * sizeof(MeteorologicalRecord));
}

void freeLog(MeteorologicalLog* log) {
    free(log->records);
    log->records = NULL;
    log->size = 0;
    log->capacity = 0;
}

void addRecord(MeteorologicalLog* log, MeteorologicalRecord rec) {
    if (log->size >= log->capacity) {
        log->capacity *= 2;
        log->records = (MeteorologicalRecord*)realloc(log->records, log->capacity * sizeof(MeteorologicalRecord));
    }
    log->records[log->size++] = rec;
}

void deleteByDate(MeteorologicalLog* log, int d, int m, int y) {
    int found = 0;
    for (int i = 0; i < log->size;) {
        MeteorologicalRecord r = log->records[i];
        if (r.day == d && r.month == m && r.year == y) {
            for (int j = i; j < log->size - 1; j++) {
                log->records[j] = log->records[j + 1];
            }
            log->size--;
            found = 1;
        } else {
            i++;
        }
    }
    if (found) {
        printf("Запись по дате %02d.%02d.%d удалена\n", d, m, y);
    } else {
        printf("Для данной даты %02d.%02d.%d записи нет\n", d, m, y);
    }
}

void showByMonth(const MeteorologicalLog* log, int m, int y) {
    int found = 0;
    for (int i = 0; i < log->size; i++) {
        MeteorologicalRecord r = log->records[i];
        if (r.month == m && r.year == y) {
            printRecord(&r);
            found = 1;
        }
    }
    if (!found) {
        printf("Записи для данной даты %02d.%d не найдены\n", m, y);
    }
}

