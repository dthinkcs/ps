#include <bits/stdc++.h>
using namespace std;


int fib(int n) {
    int curr = 0;
    int next = 1;
    for (int i = 1; i <= n; i++) {
        int next_next = curr + next;
        curr = next;
        next = next_next; 
    }

    return curr;
}

int main(void) {
    cout << fib(5) << endl;
    cout << fib(6) << endl;
    cout << fib(8) << endl;

    int x;
    cin >> x;
    cout << x << endl;
}
