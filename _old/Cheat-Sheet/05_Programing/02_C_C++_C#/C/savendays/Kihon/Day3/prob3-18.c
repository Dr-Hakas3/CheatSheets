#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int n;
    srand((unsigned)time(NULL));
    n = rand() % 46 + -10;
    printf("摂氏%d度\n", n);
    if (30 <= n)
    {
        printf("真夏日です。\n");
    }
    else if (25 <= n && n < 30)
    {
        printf("夏日です。\n");
    }
    else if (n < 0)
    {
        printf("真冬日です。\n");
    }
    return 0;
}