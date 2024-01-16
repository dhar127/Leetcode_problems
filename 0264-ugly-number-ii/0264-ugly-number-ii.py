class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[0]*n
        dp[0]=1
        p1,p2,p3=0,0,0
        for i in range(1,n):
            tm=dp[p1]*2
            ttm=dp[p2]*3
            fm=dp[p3]*5
            dp[i]=min(tm,ttm,fm)
            if dp[i]==tm: p1+=1
            if dp[i]==ttm: p2+=1
            if dp[i]==fm: p3+=1
        return dp[n-1]
        