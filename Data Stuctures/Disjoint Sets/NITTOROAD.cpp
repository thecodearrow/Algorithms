
//https://www.spoj.com/problems/NITTROAD/
#include<bits/stdc++.h>
using namespace std;
#define ll long long

class DisjointSet{
    vector<long long int>parent;
    vector<long long int>rank;
     vector<long long int>size;

    public:
        DisjointSet(long long int n){
         
          for(long long int i=0;i<=n;i++){
              parent.push_back(i);
              rank.push_back(0);
              size.push_back(1);
          }
         

        }
        long long int getSize(long long int node){
            return this->size[node];
        }

        long long int find(long long int node){
            if(node!=this->parent[node]){
                this->parent[node]=this->find(this->parent[node]);
            }
            return this->parent[node];

        }

        void ds_union(long long int u,long long int v){
            long long int leader_u=this->find(u);
            long long int leader_v=this->find(v);
            
            if(this->rank[leader_v]>this->rank[leader_u]){
                this->parent[leader_u]=leader_v; 
                this->size[leader_v]+=this->size[leader_u];
            }
            else{
                this->parent[leader_v]=leader_u;
                this->size[leader_u]+=this->size[leader_v];
                if(this->rank[leader_v]==this->rank[leader_u]){
                    this->rank[leader_u]+=1;
                }
            }
        }
        

};
int main(){
ll int t;
cin>>t;
while (t!=0){
    t-=1;
    ll int n,q,roads_added=0,h1,h2;
    cin>>n;
    DisjointSet ds=DisjointSet(n);
    vector<pair<ll int,ll int>> snapshot;
    snapshot.push_back(make_pair(0,0)); //so it starts from 1
    for(ll int i=1;i<n;i++){
        cin>>h1>>h2;
        snapshot.push_back(make_pair(h1,h2));
    }
    cin>>q;
    ll int total_pairs=((n*(n-1))/2);
    vector<ll int> answer;
    vector<string> query;
    set<ll int> removed_edges;
    for(ll int i=0;i<q;i++){
        string temp;
        cin>>temp;
        if(temp=="R"){
            cin>>temp;
            removed_edges.insert(stoi(temp));
        }
        query.push_back(temp);
    }

    for(ll int i=1;i<n;i++){
        if(removed_edges.find(i)==removed_edges.end()){
             h1=snapshot[i].first;
             h2=snapshot[i].second;
             if(ds.find(h1)!=ds.find(h2)){
             total_pairs-=ds.getSize(ds.find(h1))*ds.getSize(ds.find(h2));
             ds.ds_union(h1,h2);
             }
        }
    }
    reverse(query.begin(),query.end());
    for(int i=0;i<q;i++){
        string s=query[i];
        if(s=="Q"){
            answer.push_back(total_pairs);
        }
        else{
            ll int h1,h2,r;
            r=stoi(s);
            h1=snapshot[r].first;
            h2=snapshot[r].second;
            if(ds.find(h1)!=ds.find(h2)){
                total_pairs-=(ds.getSize(ds.find(h1))*ds.getSize(ds.find(h2)));
                ds.ds_union(h1,h2);
            }


        }
    }
    reverse(answer.begin(),answer.end());
    for(int i=0;i<answer.size();i++){
        cout<<answer[i]<<"\n";
    }
    
cout<<"\n";

}


}
