#include <iostream>
using namespace std;

int main()
{
  int n;
  cin >> n;
  int count = 0;
  while (n)
  {
    count += 1;
    n = n & (n - 1);
  }
  cout << count << endl;
}
