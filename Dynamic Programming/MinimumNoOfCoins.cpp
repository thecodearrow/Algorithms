/*
Given a value V, if we want to make change for V cents, 
and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, 
what is the minimum number of coins to make the change?

*/

#include<bits/stdc++.h>
using namespace std;
int main(){
array<int,1000> dp;
int coins[] =  {1,2,3,100};
int n=100;
dp[0]=0;
//setting default to infinity 
for(int i=1;i<=n;i++){

	dp[i]=100000;
}
for(auto c:coins){
for(int i=1;i<=n;i++){
	if(i>=c)
	dp[i]=min(dp[i],dp[i-c]+1);
}

}
cout<<dp[n];
return 0;
}

