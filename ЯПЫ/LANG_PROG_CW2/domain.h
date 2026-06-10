#ifndef DOMAIN_H
#define DOMAIN_H

typedef struct {
    int day;
    int month;
    int year;
    double temperature;
    double pressure;
    char precipitation[20];
} MeteorologicalRecord;

void printRecord(const MeteorologicalRecord* r);

#endif
