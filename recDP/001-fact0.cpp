#include <bits/stdc++.h>
using namespace std;

long long fact(int n) {
    if (n == 0) {
        return 1;
    }
    return n * fact(n - 1);
}

int main() {
    cout << fact(5) << endl; // 120 
    cout << fact(7) << endl; // 5040
} 