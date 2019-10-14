//https://practice.geeksforgeeks.org/problems/set-bits/0
#include <iostream>
using namespace std;

int main() {
	//code
	int t,b;
	cin>>t;
	while(t!=0){
	    t-=1;
	    cin>>b;
	    int count=0;
	    while(b!=0){
	        count+=1;
	        b-=(b&-b);//unset last set_bit
	    }
	    cout<<count<<"\n";
	}
	return 0;
}