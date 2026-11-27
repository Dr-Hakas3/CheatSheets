#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int n;
    srand((unsigned)time(NULL));
    n = rand() % 100 + 1;
    printf("%d\n", n);
    if (0 == n % 2)
    {
        if (0 == n % 3)
        {
            printf("２と３の公倍数です。\n");
        }
        else
        {
            printf("２の倍数です。\n");
        }
    }
    else if (0 == n % 3)
    {
        printf("３の倍数です。\n");
    }
    return 0;
}