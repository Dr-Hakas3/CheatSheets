#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int n;
    srand((unsigned)time(NULL));
    n = rand() % 6 + 1;
    printf("数値：%d\n", n);
    if (n >= 3)
    {
        printf("３以上です。\n");
    }
    return 0;
}