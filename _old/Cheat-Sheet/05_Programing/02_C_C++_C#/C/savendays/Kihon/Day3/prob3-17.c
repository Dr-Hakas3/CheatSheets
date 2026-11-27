#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int n;
    srand((unsigned)time(NULL));
    n = rand() % 100 + 1;
    printf("%d\n", n);
    if (n <= 50 && n % 2 == 0)
    {
        printf("５０以下の偶数です。\n");
    }
    else if (n <= 50)
    {
        printf("５０以下です。\n");
    }
}