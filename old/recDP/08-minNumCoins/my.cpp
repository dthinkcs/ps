#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

int fn(int n, vector<int> denoms) {
  // Write your code here.
	if (n < 0)
		return 10000; // repr of INT_MAX + 1 is gonna be INT_MIN
	if (n == 0)
		return 0;
	if (denoms.size() == 0)
		return 10000;
	vector<int> nv(denoms.begin(), denoms.end() - 1);
	return min(1 + fn(n - denoms[denoms.size() - 1], denoms), fn(n, nv));


}

int minNumberOfCoinsForChange(int n, vector<int> denoms) {

	int ans = fn(n, denoms);
	return ans < 10000 ? ans : -1;
}
