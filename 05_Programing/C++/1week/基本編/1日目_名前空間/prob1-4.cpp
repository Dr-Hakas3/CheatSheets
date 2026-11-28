#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    b = 2;
    string s, t, r;
    s = "数字を入力してください：";
    t = "を2倍した数は、";
    r = "です。";
    cin >> a;
    c = a * b;
    cout << s << endl;
    cout << a << t << c << r << endl;
    return 0;
}