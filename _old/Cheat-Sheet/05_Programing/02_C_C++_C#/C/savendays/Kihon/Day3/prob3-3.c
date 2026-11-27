#include <stdio.h>

int main(int argc, char **argv)
{
    int num;
    printf("整数を入力してください。\n");

    scanf("%d", &num);
    if (50 > num)
    {
        printf("５０未満です。\n");
    }
    return 0;
}