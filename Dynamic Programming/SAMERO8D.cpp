//https://www.spoj.com/problems/SAMER08D/
#include<bits/stdc++.h>
using namespace std;
int memo[1100][1100];
int len[1100][1100];
int LCS(string &s1,string &s2,int l1,int l2,int K){
    for(int i=0;i<l1;i++){
        for(int j=0;j<l2;j++){
            memo[i][j]=max(memo[i-1][j],memo[i][j-1]);
            if(s1[i]==s2[j]){
                if(i>0 && j>0){
                len[i][j]=len[i-1][j-1]+1;
                }
                else{
                    len[i][j]=1;
                }
            }
            if(len[i][j]>=K){
                for(int z=K;z<=len[i][j];z++){
                    memo[i][j]=max(memo[i][j],memo[i-z][j-z]+z);
                }
            }
        }
    }

    return memo[l1-1][l2-1];
}

int main(){
    int l1,l2,i,j,K;
    string s1,s2;
    while(1){
       cin>>K;
       if(K==0){
        break;
       }
        cin>>s1>>s2;
        l1=s1.size();
        l2=s2.size();
        for(i=0;i<l1;i++){
            for(j=0;j<l2;j++){
                memo[i][j]=-1;
                len[i][j]=0;
            }
        }
         cout<<LCS(s1,s2,l1,l2,K)<<"\n";   

}
}