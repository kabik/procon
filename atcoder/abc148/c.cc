#include <iostream>

using namespace std;

long gcd(long n, long m) {
    long tmp;
    while (n % m != 0) {
        tmp = m;
        m = n % m;
        n = tmp;
    }
    return m;
}

int main() {
    long a, b;
    cin >> a >> b;

    cout << a * b / gcd(a, b);

    return 0;
}
