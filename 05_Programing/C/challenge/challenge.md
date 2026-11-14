---
title: Challenge
nav_order: 1
has_children: true
parent: C
grand_parent: Programming
---
# 1. h/km -> s/m
userが入力した時速〇〇キロメートルを秒速△△メートルに変換するプログラム

```
時速（km/h）→秒速（m/s）の変換は、単位変換を正しく分解すると以下になります。

1 km = 1000 m
1 hour = 3600 seconds

したがって、

m/s=
3600
km/h×1000
	​

=km/h×
18
5
```
	​

Cプログラム
```c
#include <stdio.h>

int main(void) {
    double kmh;
    double ms;

    printf("時速(km/h)を入力してください: ");
    scanf("%lf", &kmh);

    ms = kmh * 5.0 / 18.0;

    printf("秒速: %.2f m/s\n", ms);

    return 0;
}
```
ポイント
doubleを使うことで小数精度を確保
5.0 / 18.0 にして整数除算を回避
%.2fで小数第2位まで表示

## エラーチェック付き

```c
#include <stdio.h>

int main(void) {
    double kmh;
    double ms;
    int result;

    printf("時速(km/h)を入力してください: ");

    // 入力チェック（数値以外を弾く）
    result = scanf("%lf", &kmh);

    if (result != 1) {
        printf("エラー: 数値を入力してください。\n");
        return 1;
    }

    // 負の値チェック
    if (kmh < 0) {
        printf("エラー: 負の値は入力できません。\n");
        return 1;
    }

    ms = kmh * 5.0 / 18.0;

    printf("秒速: %.2f m/s\n", ms);

    return 0;
}
```

---

# 2. 
以下は「和暦（令和・平成・昭和・大正）＋月日」を入力すると曜日を表示するCプログラムです。
mktime() を使って曜日判定しています。

■ 入力形式
R 6 5 8

意味：令和6年5月8日

対応記号：

- R = 令和 (Reiwa)
- H = 平成 (Heisei)
- S = 昭和 (Showa)
- T = 大正 (Taisho)
■ Cプログラム
```c
#include <stdio.h>
#include <time.h>
#include <string.h>

int convert_wareki_to_ad(char era, int year) {
    switch (era) {
        case 'R': return 2018 + year; // Reiwa 1 = 2019
        case 'H': return 1988 + year; // Heisei 1 = 1989
        case 'S': return 1925 + year; // Showa 1 = 1926
        case 'T': return 1911 + year; // Taisho 1 = 1912
        default: return -1;
    }
}

int main() {
    char era;
    int year, month, day;

    printf("和暦を入力 (R/H/S/T 年 月 日): ");
    if (scanf(" %c %d %d %d", &era, &year, &month, &day) != 4) {
        printf("入力形式が正しくありません。\n");
        return 1;
    }

    int ad_year = convert_wareki_to_ad(era, year);
    if (ad_year == -1) {
        printf("無効な元号です。\n");
        return 1;
    }

    struct tm t = {0};
    t.tm_year = ad_year - 1900;
    t.tm_mon = month - 1;
    t.tm_mday = day;

    if (mktime(&t) == -1) {
        printf("日付が不正です。\n");
        return 1;
    }

    char *week[] = {
        "日曜日", "月曜日", "火曜日", "水曜日",
        "木曜日", "金曜日", "土曜日"
    };

    printf("曜日: %s\n", week[t.tm_wday]);

    return 0;
}
```

■ 補足
tm_wday は 0=日曜 ～ 6=土曜
mktime() が自動で正規化＆曜日計算
入力チェックも最低限実装済み

## Python版

以下は「和暦＋月日」を入力すると曜日を返すPython版です。C版と同じロジックで、標準ライブラリだけで動きます。

■ Pythonプログラム（和暦→曜日判定）

```python
from datetime import datetime

def wareki_to_seireki(era: str, year: int) -> int:
    era = era.upper()

    if era == "R":   # 令和
        return 2018 + year  # 令和1年 = 2019
    elif era == "H": # 平成
        return 1988 + year  # 平成1年 = 1989
    elif era == "S": # 昭和
        return 1925 + year  # 昭和1年 = 1926
    elif era == "T": # 大正
        return 1911 + year  # 大正1年 = 1912
    else:
        return None


def main():
    print("和暦を入力してください（例: R 6 5 8）")
    
    try:
        era, year, month, day = input("> ").split()
        year = int(year)
        month = int(month)
        day = int(day)

        seireki = wareki_to_seireki(era, year)
        if seireki is None:
            print("無効な元号です")
            return

        dt = datetime(seireki, month, day)

        weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

        print("曜日:", weekdays[dt.weekday()])

    except ValueError:
        print("入力形式が正しくありません（例: R 6 5 8）")


if __name__ == "__main__":
    main()
```

■ ポイント
datetimeで曜日計算（内部でZellerの公式相当を処理）
weekday()は 0=月曜 ～ 6=日曜
和暦→西暦変換テーブルはC版と同じ設計

---

# 3. 