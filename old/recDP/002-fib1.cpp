#include <bits/stdc++.h>
using namespace std;

int fibH(int n, vector<int>& memo) {
    if (memo[n] != -1) {
        return memo[n];
    }
    if (n <= 1) {
        return n;
    }
    memo[n] = fibH(n - 1, memo) + fibH(n - 2, memo);
    return memo[n];
}

int fib(int n) {
    vector<int> memo(n + 1, -1);

    return fibH(n, memo);
}

int main(void) {
    cout << fib(5) << endl;
    cout << fib(6) << endl;
    cout << fib(8) << endl;
}
