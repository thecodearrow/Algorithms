

cost=[0,1, 5, 8, 9, 10, 17, 17, 20]
n=8 

rod_cut=[0]*(n+1)


for i in range(1,n+1):
    val=0
    for j in range(1,i+1):
        val=max(val,cost[j]+rod_cut[i-j])
    rod_cut[i]=val
    
print(rod_cut[8])