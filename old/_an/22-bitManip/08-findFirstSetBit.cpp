int returnFirstSetBit(int n){

    // return n & (~(n & (n - 1))); // x~x = 0
       return n & (-n);
}
