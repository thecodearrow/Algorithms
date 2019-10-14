//https://practice.geeksforgeeks.org/problems/swap-two-nibbles-in-a-byte/0

#include <iostream>
using namespace std;

int main() {

	int t;
	cin>>t;
	while(t!=0){
	    t-=1;
	    int n;
	    cin>>n;
	    int left_nibble=n>>4;
	    int left_nibble_plus_4_zeros=left_nibble<<4;
	    int right_nibble=(n-left_nibble_plus_4_zeros);
	    int right_nibble_plus_4_zeros=right_nibble<<4;
	    int swapped_number=right_nibble_plus_4_zeros+left_nibble;
	    cout<<swapped_number<<"\n";
	    
	    
	}
	return 0;
}

