#include <stdio.h>

int main(int argc, char **argv)
{
    int a;
    printf("数値を入力：");
    //  キーボードから整数を入力
    scanf("%d", &a);
    //  入力した値が、正の数かどうか調べる
    if (a > 0)
    {
        printf("入力した値は、正の数です。\n"); //   正の数だった場合に実行
    }
    else
    {
        printf("入力した値は、正の数ではありません。\n"); //   0か負のかずだった場合に実行
    }
}