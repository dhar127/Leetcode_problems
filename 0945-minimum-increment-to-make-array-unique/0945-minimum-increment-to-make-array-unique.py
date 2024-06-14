class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        m=0
        f=0
        for i in nums:
            m=max(m,i)
            f+=(m-i)
            m+=1
        return f