class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        mem=[[0 for _ in range (len(matrix[0])+1)] for __ in range(len(matrix)+1)]
        a=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    mem[i+1][j+1]=min(mem[i+1][j],mem[i][j+1],mem[i][j])+1
                    a=max(a,mem[i+1][j+1])
        
        return a*a
        