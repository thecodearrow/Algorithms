//https://practice.geeksforgeeks.org/problems/bit-difference/0


#include <iostream>
using namespace std;

int main() {
	//Find a xor b
	//No. of set bits in a xor b is the flips reqd. to get from a to b
	int t;
	cin>>t;
	while(t!=0){
	    t-=1;
	    int a,b;
	    cin>>a;
	    cin>>b;
	    int number=a^b;
	    int flips=0;
	    while(number){
	        flips+=1;
	        number=(number&(number-1));
	    }
	    cout<<flips<<"\n";
	}
	return 0;
}