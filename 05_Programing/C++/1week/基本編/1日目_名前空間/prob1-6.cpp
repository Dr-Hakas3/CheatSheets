#include <iostream>

using namespace std;

// int a = 0, b = 0, c = 0, d = 0;
// string s = NULL, t = NULL, r = NULL, i = NULL, n = NULL;
string a;
string b;

string s = "姓を入力：";
string t = "名を入力：";

int main()
{
    cout << s;
    cin >> a;
    cout << t;
    cin >> b;
    string r = a + b;
    string i = "名前は「" + r + "」です。";
    cout << i << endl;
    return 0;
}
