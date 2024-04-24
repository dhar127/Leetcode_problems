class Solution:
    def tribonacci(self, n: int) -> int:
        x=[0,1,1]
        for i in range(3,n+1):
            x.append(x[i-1]+x[i-2]+x[i-3])
        return x[n] 
            
        