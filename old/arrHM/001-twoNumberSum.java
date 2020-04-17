/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
    public static List<Integer> twoNumberSum(List<Integer> arr, int target) {
        Set<Integer> seen = new HashSet<>();
        List<Integer> ans = new ArrayList<>();
        for (int num: arr) {
            if (seen.contains(target - num)) {
                 ans.add(num); 
                 ans.add(target-num);
                 return ans;
            }
            seen.add(num);
        }
        return ans;
    }
    
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while ((T--) != 0) {
	    
    	    int n;
    	    n = sc.nextInt();
    	    
    	    int target;
    	    target = sc.nextInt();
    
    	    
    	    List<Integer> v = new ArrayList<>();
    	    for (int i = 0; i < n; i++) {
    	        v.add(sc.nextInt());
    	    }
    	    
    	    
    	    List<Integer> ans = twoNumberSum(v, target);
    	    
    	    if (ans.size() != 0) {
    	        System.out.println("Yes");
    	    } else {
    	        System.out.println("No");
    	    }
	    }

	}
}