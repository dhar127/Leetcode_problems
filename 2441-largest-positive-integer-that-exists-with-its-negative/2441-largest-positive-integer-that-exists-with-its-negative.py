class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if (-1*i) in nums:
                l.append(i)
        if len(l)==0:
            return -1
        return max(l)
        