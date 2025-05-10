#include <stdio.h>

int main() {
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        return 1;
    }
    char c = getc(file);
    int num = -1;
    while (c != EOF && c >= '0' && c <= '9') {
        if (num < 0) {
            num = c - '0';
        } else {
            num = num * 10 + c - '0';
        }
        printf("%d ", num);
        c = getc(file);
    }
    printf("%d", num);
    fclose(file);
    return 0;
}