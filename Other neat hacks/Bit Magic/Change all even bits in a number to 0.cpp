//https://practice.geeksforgeeks.org/problems/change-all-even-bits-in-a-number-to-0/0

#include <iostream>
using namespace std;

int main() {
	//code
	int t;
	cin>>t;
	while(t!=0){
	    t-=1;
	    int n;
	    cin>>n;
	    int ans=0;
	    for(int i=1;i<32;i+=2){
	    ans+=n&(1<<i);
	}
	cout<<ans<<"\n";
	}
	return 0;
}