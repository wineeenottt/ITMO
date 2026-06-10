#include <stdio.h>
#include <stdlib.h>

void encrypt(char* str, int key) {
    printf("Кодировка: ");
    while (*str != '\0') {
        int curChar = (int)*str;
        if (curChar >= 65 && curChar <= 122) {
            int curCode = (int) *str + key;
            if (curCode > 122) {
                curCode -= 122;
            }
            printf("%c", curCode);
        }
        else {
            printf("%c", *str);
        }
        str++;
    }
    printf("\n");
}

void decrypt(char* str, int key) {
    printf("Декодировка: ");
    while (*str != '\0') {
        int curChar = (int)*str;
        if (curChar >= 65 && curChar <= 122) {
            int curCode = (int) *str - key;
            if (curCode < 65) {
                curCode += 122 - 65;
            }
            printf("%c", curCode);
        }
        else {
            printf("%c", *str);
        }
        str++;
    }
    printf("\n");
}


int main(int argc, char** argv) {
    char* text = argv[1];
    int key = atoi(argv[2]);

    printf("Исходный текст: %s\n", text);
    printf("Ключ: %d\n", key);

    encrypt(text, key);
    decrypt(text, key);
    return 0;
}