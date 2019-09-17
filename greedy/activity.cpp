#include <bits/stdc++.h>
using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
  // sorting in ascending order
  return a.second < b.second;
}

int main()
{
  int T;
  cin >> T;
  while (T--)
  {
    int N;
    cin >> N;
    int* s = new int[N];
    int* f = new int[N];
    for (int i = 0; i < N; i++)
      cin >> s[i];
    for (int i = 0; i < N; i++)
      cin >> f[i];

    vector<pair<int, int>> v;
    for (int i = 0; i < N; i++)
      v.push_back({s[i], f[i]});
    sort(v.begin(), v.end(), compare);
    // for (int i = 0; i < N; i++)
    //   cout << v[i].first << " " << v[i].second << endl;

    int i = 0;
    int count = 1;
    for (int j = 1; j < N; j++)
    {
      if (v[i].second <= v[j].first) {
        count++;
        i = j;
      }
    }
    cout << count << endl;
  }
}
