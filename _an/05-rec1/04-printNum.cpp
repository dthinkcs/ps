void print(int n){
    if(n == 1){
        cout << n << " ";
    }
    cout << n << " ";
    print(n - 1);
}
