#include <stdio.h>

int main(int argc)
{
    int num;
    printf("整数を入力してください\n");
    scanf("%d", &num);
    if (10 >= num || 90 <= num)
    {
        printf("１０以下か９０以上です。\n");
    }
    return 0;
}