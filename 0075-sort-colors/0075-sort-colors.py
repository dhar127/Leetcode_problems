class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        g=nums.copy()
        for i in range(len(g)):
            for j in range(i,len(g)):
                if g[i]>g[j]:
                    t=g[i]
                    g[i]=g[j]
                    g[j]=t
        j=0
        for i in range(len(nums)):
            nums[j]=g[i]
            j+=1
        