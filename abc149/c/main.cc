#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int MAX = 110000;
    bool isComposite[MAX];
    for (int i = 2; i < MAX; i++) {
        isComposite[i] = false;
    }

    for (int i = 2; i < MAX; i++) {
        if (!isComposite[i]) {
            if (i >= n) {
                cout << i;
                break;
            }
            for (int j = 2 * i; j < MAX; j += i) {
                isComposite[j] = true;
            }
        }
    }

    return 0;
}
