#include <iostream>
#include <set>

using namespace std;

int main() {
    int n;
    int p[8];
    int q[8];
    int kaijou[9] = {1, 1, 2, 6, 24, 120, 720, 5040};
    int used[9] = {1, 0, 0, 0, 0, 0, 0, 0, 0};
    int used2[9] = {1, 0, 0, 0, 0, 0, 0, 0, 0};

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> q[i];
    }

    int a = 0;
    for (int i = 0; i < n; i++) {
        int cnt = 0; // unused
        int num = p[i];
        used[ num ] = 1;
        for (int k = num; k > 0; k--) {
            if (used[k] == 0) { cnt++; }
        }
        a += cnt * kaijou[ n-i-1 ];
    }


    int b = 0;
    for (int i = 0; i < n; i++) {
        int cnt = 0; // unused
        int num = q[i];
        used2[ num ] = 1;
        for (int k = num; k > 0; k--) {
            if (used2[k] == 0) { cnt++; }
        }
        b += cnt * kaijou[ n-i-1 ];
    }


    if (a > b) { cout << a-b; }
    else { cout << b-a; }

    return 0;
}
