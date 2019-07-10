#include <iostream>
#include <climits>
using namespace std;
// secondMax =/= max Ex: 10, 10, 10 -> iNT_MIN( dne )
int secondMax(int* arr, int n)
{
	int largest = INT_MIN;
	int secondLargest = INT_MIN;
	for (int i = 0; i < n; i++)
	{
		if (arr[i] > largest)
		{
			secondLargest = largest;
			largest = arr[i];
		}
		else if (largest > arr[i] && arr[i] > secondLargest)
			secondLargest = arr[i];
	}
	return secondLargest;
}

int main()
{
	int t;
	cin >> t;
	int arr[1000000];
	while(t--)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> arr[i];
		cout << secondMax(arr, n);
		
	}
return 0;
}
