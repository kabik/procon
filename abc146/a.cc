#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;

    int n = 0;
    if (s == "SUN") { n = 7; }
    if (s == "MON") { n = 6; }
    if (s == "TUE") { n = 5; }
    if (s == "WED") { n = 4; }
    if (s == "THU") { n = 3; }
    if (s == "FRI") { n = 2; }
    if (s == "SAT") { n = 1; }
    cout << n;

    return 0;
}
