#include <stdio.h>

int main(int argc, char **argv)
{
    int dice;
    printf("１から６の数値を入力してください：");
    scanf("%d", &dice);

    if (1 <= dice && dice <= 6)
    {

        if (dice == 2 || dice == 4 || dice == 6)
        {
            printf("丁です。\n");
        }
        else
        {
            printf("半です。\n");
        }
    }
    else
    {
        printf("範囲外の数値です。\n");
    }
    return 0;
}