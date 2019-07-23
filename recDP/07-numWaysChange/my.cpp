#include <vector>
using namespace std;

int numberOfWaysToMakeChange(int n, vector<int> denoms) {
  // Write your code here.
	if (n < 0)
		return 0; // no ways of making change
	if (n == 0)
		return 1;
	if (denoms.size() == 0)
		return 0;
	vector<int> newVec(denoms.begin(), denoms.end() - 1);
	return numberOfWaysToMakeChange(n - denoms[denoms.size() - 1], denoms) + numberOfWaysToMakeChange(n, newVec);

}
//-----------
