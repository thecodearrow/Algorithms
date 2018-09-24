"""

Given an integer representing a given amount of change, write a
function to compute the total number of coins required to make
that amount of change. You can assume that there is always a
1¢ coin.

eg. (assuming American coins: 1, 5, 10, and 25 cents)
makeChange(1) = 1 (1)
makeChange(6) = 2 (5 + 1)
makeChange(49) = 7 (25 + 10 + 10 + 1 + 1 + 1 + 1)

"""



#https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins, amount):
      
        MAX_INT=10**9+7
        dp=[]
        coins=sorted(coins)
        for i in range(amount+1):
            dp.append(MAX_INT)
        
        dp[0]=0
        
        for c in coins:
            for amt in range(1,amount+1):
                if(amt-c>=0):
                    dp[amt]=min(dp[amt-c]+1,dp[amt]) 
        
        if(dp[amount]>=MAX_INT):
            return -1
        return dp[amount]
        
