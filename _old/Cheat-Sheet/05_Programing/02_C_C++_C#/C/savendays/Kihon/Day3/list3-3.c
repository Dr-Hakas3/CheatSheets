#include <stdio.h>

int main(int argc, char **argv)
{
    int num;
    printf("１〜３の値を入力してください：");
    //     キーボードから整数を入力
    scanf("%d", &num);
    //  入力した値が、正の数かどうかを調べる
    if (num == 1)
    {
        printf("one\n"); //  numが１だった場合の処理
    }
    else if (num == 2)
    {
        printf("two\n"); //  numが２だった場合の処理
    }
    else if (num == 3)
    {
        printf("three\n"); //  numが３だった場合
    }
    else
    {
        printf("不適切な値です。\n"); //  それ以外の値が入力させた場合
    }
    return 0;
}