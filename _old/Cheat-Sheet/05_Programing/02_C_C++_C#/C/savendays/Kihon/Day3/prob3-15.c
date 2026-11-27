#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int n;
    srand((unsigned)time(NULL));
    n = rand() % 100 + 1;
    printf("%d\n", n);
    if (n > 80)
    {
        printf("優\n");
    }
    else if (80 > n && n >= 70)
    {
        printf("良\n");
    }
    else if (70 > n && n >= 60)
    {
        printf("可\n");
    }
    else
    {
        printf("不可\n");
    }
    return 0;
}