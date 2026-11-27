#include <stdio.h>

int main(int argc, char **argv)
{
    int num;
    printf("１〜３の値を入力してください：");

    if (scanf("%d", &num) != 1)
    {
        printf("入力エラーです。\n");
        return 1;
    }

    switch (num)
    {
    case 1:
        printf("one\n");
        break;
    case 2:
        printf("two\n");
        break;
    case 3:
        printf("three\n");
        break;
    default:
        printf("不適切な値です。\n");
        break;
    }
    return 0;
}