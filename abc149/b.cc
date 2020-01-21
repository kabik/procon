#include <iostream>

using namespace std;

int main() {
    long a, b, k;
    cin >> a >> b >> k;

    if (a < k) {
        k -= a;
        a = 0;
        b = (b < k) ? 0 : b-k;
    } else {
        a -= k;
    }

    cout << a << " " << b;

    return 0;
}
