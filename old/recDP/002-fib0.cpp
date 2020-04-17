#include <bits/stdc++.h>
using namespace std;

int fib(int n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

int main(void) {
    cout << fib(5) << endl;
    cout << fib(6) << endl;
    cout << fib(8) << endl;
}
