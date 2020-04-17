#include <iostream>
#include <vector>
using namespace std;

void diceHelper(int diceLeft, vector<int>& chosen) {
  if (diceLeft == 0) {
    for (int i = 0; i < chosen.size(); i++)
      cout << chosen[i] << " ";
    cout << endl;

  } else {
    // some dice left to roll
    // handle one die
    // for each value that die could have
    for (int i = 1; i <= 6; i++) {
      // choose i
      chosen.push_back(i); // ex: {1, 1, 1}, {1, 1, 2} ... {1, 1, 6}
      // explore i
      diceHelper(diceLeft - 1, chosen); // ex: get those printed
      // unchoose
      chosen.erase(chosen.end() - 1); // ex: {1, 1} so that you can {1, 1, 2}..... can also use chose.pop_back();
    }
  }
}

int main() {
  vector<int> v;
  int n;
  cin >> n;
  diceHelper(n, v);
}
