#https://www.youtube.com/watch?v=oDhu5uGq_ic

def maxProfitWithKTransactions(prices, k):
	days=len(prices)
	if(days==0):
		return 0
    profit=[[0 for d in range(days)] for i in range(k+1)]
	for i in range(1,k+1):
		maxDiff=-float("inf")
		for j in range(1,days):
			maxDiff=max(maxDiff,-prices[j-1]+profit[i-1][j-1])
			noSellProfit=profit[i][j-1]
			sellProfit=prices[j]+maxDiff
			profit[i][j]=max(noSellProfit,sellProfit)
	
	return profit[k][days-1]
			
