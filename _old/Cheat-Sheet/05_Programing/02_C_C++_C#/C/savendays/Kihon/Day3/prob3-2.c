#include <stdio.h>

int main(int argc, char **argv)
{
    int num;
    printf("整数の値を入力してください。：\n");

    scanf("%d", &num);
    if (num != 1)
    {
        printf("１ではありません。\n");
    }
    return 0;
}