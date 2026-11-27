#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int n;
    srand((unsigned)time(NULL));
    n = rand() % 10 + 1;
    printf("数値：%d\n", n);
    if (n != 1)
    {
        printf("１ではありません。\n");
    }
    else
    {
        printf("１です。\n");
    }
}