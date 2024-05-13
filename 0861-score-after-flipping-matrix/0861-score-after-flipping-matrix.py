class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        for i in range(m):
            s = ''.join(map(str,grid[i]))
            dec = int(s,2)
            if dec^int('1'*len(s),2)>dec:
                for j in range(n):
                    grid[i][j] = (grid[i][j]+1)%2

        for j in range(n):
            count1 = 0
            for i in range(m):
                count1+=grid[i][j]

            if count1<m-count1:
                for i in range(m):
                    grid[i][j] = (grid[i][j]+1)%2

        ans = 0
        for i in range(m):
            ans+=int(''.join(map(str,grid[i])),2)

        return ans