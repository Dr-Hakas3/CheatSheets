#include <stdio.h>

int main(int argc, char **argv)
{
    int n;
    printf("年数を入力：");
    scanf("%d", &n);
    if (n % 4 == 0)
    {
        if (n % 100 == 0)
        {
            if (n % 400 == 0)
            {
                printf("閏年です。\n");
            }
            else
            {
                printf("閏年ではありません。\n");
            }
        }
        else
        {
            printf("閏年です。\n");
        }
    }
    else
    {
        printf("閏年ではありません。\n");
    }
    return 0;
}
