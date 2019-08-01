int clearAllBits(int n, int i){
    // return n & ((1 << i) - 1)
    return n & ~(~0 << i);
}
