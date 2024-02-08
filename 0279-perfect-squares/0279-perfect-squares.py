class Solution:
    def numSquares(self, n: int) -> int:
        m=[float(inf) for _ in range(n+1)]
        m[0]=0
        l=[]
        for i in range(1,n+1):
            if i*i>n:
                break
            l.append(i*i)
        for i in range(n+1):
            for j in l:
                if i+j<=n:
                    m[i+j]=min(m[i]+1,m[i+j])
                else:
                    break
        return m[n]
        