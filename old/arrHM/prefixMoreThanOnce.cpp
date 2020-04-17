#include <iostream>
#include <string>
using namespace std;

int countReps(string s, string sub) {
  int count = 0;
  for (int i = 0; i < s.length(); i++) {
    if (s.find(sub, i) != string::npos) {
      count++;
    }
  }
  return count;
}

string fn(string s) {
   string ans = "";
   for (int i = s.length(); i > 0; --i) {
    if ( countReps( s, s.substr(0, i) ) > 1 ) {
      ans = s.substr(0, i);
      break;
    }
  }
  return ans;
}

int main() {
  string s = "ababaa";
  cout << fn(s) << endl; // "aba"
  return 0;
}
