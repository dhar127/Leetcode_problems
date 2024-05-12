class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        f=[]
        r=len(grid[0])
        c=len(grid)
        for i in range(0,r-2):
            g=[]
            for j in range(0,c-2):
                tl=[]
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        tl.append(grid[k][l])
                g.append(max(tl))
            f.append(g)
        return f
                