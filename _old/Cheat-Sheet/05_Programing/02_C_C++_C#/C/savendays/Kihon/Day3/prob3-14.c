#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int a, b;
    srand((unsigned)time(NULL));

    a = rand() % 10 + 1;
    b = rand() % 10 + 2;
    printf("%d %d\n", a, b);
    if (a > b)
    {
        printf("aのほうが大きいです。\n");
    }
    else
    {
        printf("bのほうが大きいです。\n");
    }
    return 0;
}