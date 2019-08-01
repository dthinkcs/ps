bool isPowerOf4(int n) {
    /*
    bool isPowerofTwo = n && !(n & (n - 1));
    if(!isPowerofTwo) {
        return false;
    }
    */
    return   n && ((n & (n - 1)) == 0) && !(n & 0xAAAAAAAA);

}
