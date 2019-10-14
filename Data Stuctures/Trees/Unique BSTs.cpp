//https://practice.geeksforgeeks.org/problems/unique-bsts/1

int numTrees(int n) {
    // Your code here
    double fact[30]={0};
    fact[0]=1;
    for(int i=1;i<30;i++){
        fact[i]=fact[i-1]*i;
    }
    //nth catalan number 
    int ans=(fact[2*n])/(fact[n+1]*fact[n]);
    return ans;
    
    
}

//Dynamic Programming Solution

// Functiuon to return number of trees
int calculateBST(int n,int* memo){
    if(memo[n]!=-1){
        return memo[n];
    }
    int ans=0;
    for(int i=1;i<=n;i++){
       ans+=calculateBST(i-1,memo)*calculateBST(n-i,memo); 
    }
    memo[n]=ans;
    return memo[n];
}

int numTrees(int n) {
    // Your code here
    int memo[15];
    for(int i=0;i<15;i++){
        memo[i]=-1;
    }
    memo[0]=1;
    calculateBST(n,memo);
    return memo[n];
    
}

