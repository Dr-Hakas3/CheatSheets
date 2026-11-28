#include <iostream>

using namespace std;

int a, b, c, d;
string s = "1つ目の数：";
string t = "2つ目の数：";

int main()
{
    cout << s;
    cin >> a;
    cout << t;
    cin >> b;
    c = a + b;
    d = a - b;
    cout << a << "+" << b << "=" << c << endl;
    cout << a << "-" << b << "=" << d << endl;
}
