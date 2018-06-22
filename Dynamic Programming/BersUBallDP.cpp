//code forces 489B


#include <bits/stdc++.h>
using namespace std;
#define c 110
int main() {
	// your code goes here
	vector<int> a;
    vector<int> b;
	int n,m,dp[c][c];
	 int temp;
	cin>>n;
	for(int i=0;i<n;i++){
	    cin>>temp;
	    a.push_back(temp);
	}
	sort(a.begin(),a.end());
	cin>>m;
	for(int i=0;i<m;i++){
	   
	    cin>>temp;
	    b.push_back(temp);
	}
	sort(b.begin(),b.end());
	int boy,girl,diff;
	for(int i=0;i<n;i++){
	    boy=a[i];
	    for(int j=0;j<m;j++){
	        
	      girl=b[j];
	        
	        diff=abs(girl-boy);
	       
	        if(i>0 and j>0){
	            dp[i][j]=max(dp[i][j],dp[i-1][j-1]);
	        }
	         if(diff<=1){
	            dp[i][j]++;
	        }
	        if(i>0){
	            dp[i][j]=max(dp[i][j],dp[i-1][j]);
	        }
	        if(j>0){
	            dp[i][j]=max(dp[i][j],dp[i][j-1]);
	        }
	        
	        
	        }
	    }
	

	cout<<dp[n-1][m-1];
	
	return 0;
}
















/*

#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	vector<int> a;
    vector<int> b;
    unordered_set<int> s;
	int n,m;
	 int temp;
	cin>>n;
	for(int i=0;i<n;i++){
	    cin>>temp;
	    a.push_back(temp);
	}
	sort(a.begin(),a.end());
	cin>>m;
	for(int i=0;i<m;i++){
	   
	    cin>>temp;
	    b.push_back(temp);
	}
	sort(b.begin(),b.end());
	int count=0;
	int boy,girl,diff;
	for(int i=0;i<n;i++){
	    boy=a[i];
	    for(int j=0;j<m;j++){
	        if(s.find(j)==s.end()){
	      girl=b[j];
	      diff=abs(boy-girl);
	   
	      if(diff==1 || diff==0){
	          count+=1;
	          s.insert(j);
	          break;
	      }
	        }
	    }
	}
	cout<<count;
	
	return 0;
}


*/