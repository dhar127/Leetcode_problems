class Solution:
    def minFallingPathSum(self,A: List[List[int]]) -> int:
        n=len(A)
        dp=[[ 0 for i in range(n)] for j in range(n)]
        dp[0]=A[0]
        for i in range(1,n):
            for j in range(n):
                dp[i][j]=A[i][j]+min(dp[i-1][max(0,j-1)],dp[i-1][j],dp[i-1][min(n-1,j+1)])
        return min(dp[-1])