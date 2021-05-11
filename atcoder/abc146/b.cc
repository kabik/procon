#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string s;
    cin >> n >> s;

    char aChar = 'A';
    for (int i = 0; i < s.length(); i++) {
        char c = 'A' + (s[i] - 'A' + n) % 26;
        cout << c;
    }

    return 0;
}
