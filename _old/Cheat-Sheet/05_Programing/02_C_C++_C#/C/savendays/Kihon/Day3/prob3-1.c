#include <stdio.h>

int main(int argc, char **argv)
{
    int num;
    printf("数値を入力してください：");
    scanf("%d", &num);

    if (5 <= num)
    {
        printf("５以上です。\n");
    }
    else
    {
        printf("不適切な値です。\n");
    }
    return 0;
}