#include <bits/stdc++.h>
using namespace std;


int fib(int n) {
    vector<int> dp(n + 1, 0);
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}

int main(void) {
    cout << fib(5) << endl;
    cout << fib(6) << endl;
    cout << fib(8) << endl;
}
