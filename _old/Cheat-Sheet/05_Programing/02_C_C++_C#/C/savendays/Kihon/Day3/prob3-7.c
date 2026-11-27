#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int n;
    srand((unsigned)time(NULL));
    n = rand() % 10 + 1;
    printf("数値：%d\n", n);
    if (5 <= n)
    {
        printf("５以上です。\n");
    }
    else
    {
        printf("５未満です。\n");
    }
    return 0;
}