#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;

    int len = s.length();
    int cnt = 0;
    for (int i = 0; i < len / 2; i++) {
        if ( s[i] != s[len-i-1] ) {
            cnt++;
        }
    }
    cout << cnt;

    return 0;
}
