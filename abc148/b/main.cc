#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string s, t;
    cin >> n >> s >> t;

    for (int i = 0; i < n; i++) {
        cout << s[i] << t[i];
    }

    return 0;
}
