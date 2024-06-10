class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        f=sorted(heights)
        g=0
        for i in range(len(heights)):
            if heights[i]!=f[i]:
                g+=1
        return g
        