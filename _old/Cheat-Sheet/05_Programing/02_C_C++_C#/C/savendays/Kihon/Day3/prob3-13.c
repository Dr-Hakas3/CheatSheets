#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int n;
    srand((unsigned)time(NULL));
    n = rand() % 3 + 1;
    printf("%d\n", n);
    switch (n)
    {
    case 1:
        printf("グー");
        break;
    case 2:
        printf("チョキ");
        break;
    case 3:
        printf("パー");
        break;
    default:
        break;
    }
}