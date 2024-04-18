class Solution:
    def islandPerimeter(self, l: List[List[int]]) -> int:
        a=0
        for i in range(len(l)):
            for j in range(len(l[0])):
                if l[i][j]==1:
                    if i==0:
                        a+=1
                    if j==0:
                        a+=1
                    if j>0 and l[i][j-1]==0:
                        a+=1
                    if i>0 and l[i-1][j]==0:
                        a+=1
                    if j<len(l[0])-1 and l[i][j+1]==0:
                        a+=1
                    if i<len(l)-1 and l[i+1][j]==0:
                        a+=1
                    if i==len(l)-1:
                        a+=1
                    if j==len(l[0])-1:
                        a+=1
        return a