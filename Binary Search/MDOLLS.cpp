#include<bits/stdc++.h>
using namespace std;
#define ll long long

bool cmp(const pair<int,int> &a, 
              const pair<int,int> &b) 
{     if(a.first==b.first){
    return a.second<b.second;

}
    return (a.first > b.first); 
}

int main(){
ll int t,n,w,h;

cin>>t;
while(t!=0){
    t-=1;
    vector<pair<ll int,ll int>> dolls;
    cin>>n;
    for(ll int i=0;i<n;i++){
        cin>>w>>h;
        dolls.push_back(make_pair(w,h));
    }

    sort(dolls.begin(),dolls.end(),cmp);
    vector<pair<ll int,ll int>> available_dolls;
    vector<ll int> dolls_heightwise;
    ll count=1;
    available_dolls.push_back(dolls[0]);
    dolls_heightwise.push_back(dolls[0].second);
    for(int i=1;i<n;i++){
        w=dolls[i].first;
        h=dolls[i].second;
        int pos=upper_bound(dolls_heightwise.begin(),dolls_heightwise.end(),h)-dolls_heightwise.begin();
        //cout<<w<<" "<<h<<" "<<pos<<"pos\n";
        if(pos<count){
            available_dolls[pos]=make_pair(w,h);
            dolls_heightwise[pos]=h;
        }
        else{
            available_dolls.push_back(make_pair(w,h));
            dolls_heightwise.push_back(h);
            count++;
        }

    }
    cout<<count<<"\n";
}




}