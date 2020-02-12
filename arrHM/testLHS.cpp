#include <iostream>
using namespace std;

int* fn(int* arr) {
    return arr + 1;
}

int main() {

    int* arr = new int[3];
    for (int i = 0; i < 3; i++) 
        arr[i] = 0;
    fn(arr) = 3; // lvalue and rvalue in C language
    // fn are rvalues
}
