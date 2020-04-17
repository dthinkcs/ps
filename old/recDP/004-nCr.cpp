#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// map<pair<int, int>, int> m; // otherwise own hash function frozenset in python

int C(int n, int r) {
    // if (m.count(make_pair(n, r)) != 0) {
    //     return m[make_pair(n, r)];
    // }
    // if (n < 0 || n < r) {
    //     return 0;
    // }
    // if (r == 0 || r == n) {
    //     return 1;
    // }
    // m[make_pair(n, r)] = C(n - 1, r - 1) + C(n - 1, r);
    // return m[make_pair(n, r)];
    return 1;
}

int main() {
	//code
	int T;
	cin >> T;
	while (T--) {
	    int n, r;
	    cin >> n >> r;
	    cout << C(n, r) << endl;
	}
}

