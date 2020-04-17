#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

vector<int> twoNumberSum(vector<int>& arr, int target) {
    vector<int> ans;
    unordered_set<int> seen;
    for (int num: arr) {
        if (seen.count(target - num) != 0) {
            ans.push_back(min(num, target-num));
            ans.push_back(max(num, target-num));
        }
        seen.insert(num);
    }
    return ans;
}

int main() {
	//code
	int T;
	cin >> T;
	
	while (T--) {
	    
	    int n;
	    cin >> n;
	    
	    int target;
	    cin >> target;

	    
	    vector<int> v(n);
	    for (int i = 0; i < n; i++) {
	        cin >> v[i];
	    }
	    
	    
	    vector<int> ans = twoNumberSum(v, target);
	    
	    if (ans.size() != 0) {
	        cout << "Yes" << endl;
	    } else {
	        cout << "No" << endl;
	    }
	}
	return 0;
}