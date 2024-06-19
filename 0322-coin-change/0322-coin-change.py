class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mv=amount+1
        dp=[mv]*(mv)
        dp[0]=0
        for c in coins:
            for x in range(c,amount+1):
                dp[x]=min(dp[x],dp[x-c]+1)
        return dp[amount] if dp[amount]!=mv else -1