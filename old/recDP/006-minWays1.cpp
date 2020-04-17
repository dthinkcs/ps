#include <bits/stdc++.h>
using namespace std;

int countStepsTo1H(int n, vector<int>& memo) {
    if (memo[n] != -1) 
        return memo[n];
    
    if (n <= 1) {
        return 0; // Bug1: Do Nothing is 0 because its an addition problem
    }
    int path1 = countStepsTo1H(n - 1, memo);
    int path2 = n % 2 == 0 ? countStepsTo1H(n / 2, memo) : INT_MAX;
    int path3 = n % 3 == 0 ? countStepsTo1H(n / 3, memo) : INT_MAX;
    memo[n] = 1 + min(path1, min(path2, path3)); // BUGS(3): 1 + , min can only take two arguments in c++
    return memo[n];
    
}

int countStepsTo1(int n){

    vector<int> arr(n + 1, -1); // think of this as a "cloudy" arr in the stackframe
    // int* arr = new int[n + 1];
    // for (int i = 0; i <= n; i++) {
    //     arr[i] = -1;
    // }
    
    return countStepsTo1H(n, arr);
}
