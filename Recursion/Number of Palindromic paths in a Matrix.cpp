//https://practice.geeksforgeeks.org/problems/number-of-palindromic-paths-in-a-matrix/0


#include <iostream>
using namespace std;

int palindrome(string s1,int n){
    string s2="";
    for(int i=n-1;i>=0;i--){
        s2+=s1[i];
    }
    
    if(s1==s2){
        return 1;
        
    }
    return 0;
    
}
int numWays(int i,int j,int r,int c,string s,char a[][10]){
    
    if(i>=r || j>=c){
        //out of bounds
        return 0;
    }
    if(i==r-1 && j==c-1){
        //reached the end
        s+=a[i][j];
        int n=s.length();
        if(n>0){
            if(palindrome(s,n)){
                return 1;
            }
            return 0;
        }
    }
    s+=a[i][j];
    return numWays(i+1,j,r,c,s,a)+numWays(i,j+1,r,c,s,a);
}
int main() {
	int t;
	cin>>t;
	while(t!=0){
	    t-=1;
	    int r,c;
	    cin>>r>>c;
	    char mat[10][10];
	    for(int i=0;i<r;i++)
	        for(int j=0;j<c;j++){
	            cin>>mat[i][j];
	        }
	        
	    cout<<numWays(0,0,r,c,"",mat)<<"\n";
	}
	
	return 0;
}