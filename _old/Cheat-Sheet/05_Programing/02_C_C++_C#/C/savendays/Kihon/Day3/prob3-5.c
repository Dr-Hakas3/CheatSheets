#include <stdio.h>

int main(int argc)
{
    int num;
    printf("整数を入力してください。");
    scanf("%d", &num);

    if (20 <= num || num < 80)
    {
        printf("２０以上８０未満です。\n");
    }
    return 0;
}