//https://www.spoj.com/problems/AIBOHP/
#include<bits/stdc++.h>
using namespace std;
int memo[6110][6110];
int minInsertions(int i,int j,string &s){
    if(i>=j){
        return 0;
    }
    if(memo[i][j]!=-1){
        return memo[i][j];
    }
    if(s[i]==s[j]){
        memo[i][j]=minInsertions(i+1,j-1,s);
    }
    else{
        memo[i][j]=1+min(minInsertions(i,j-1,s),minInsertions(i+1,j,s));
    }
    return memo[i][j];
}

int main(){
    int t;
    cin>>t;
    while(t!=0){
        t-=1;
        string s;
        cin>>s;
        int n=s.size();
        for(int i=0;i<=n;i++){
            for(int j=0;j<=n;j++){
                memo[i][j]=-1;
            }
        }
        cout<<minInsertions(0,n-1,s);
        cout<<"\n";
    }
}