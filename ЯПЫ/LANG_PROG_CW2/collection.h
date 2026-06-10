#ifndef COLLECTION_H
#define COLLECTION_H

#include "domain.h"

typedef struct {
    MeteorologicalRecord* records;
    int size;
    int capacity;
} MeteorologicalLog;

void initLog(MeteorologicalLog* log);
void freeLog(MeteorologicalLog* log);

void addRecord(MeteorologicalLog* log, MeteorologicalRecord rec);
void deleteByDate(MeteorologicalLog* log, int d, int m, int y);
void showByMonth(const MeteorologicalLog* log, int m, int y);

#endif
