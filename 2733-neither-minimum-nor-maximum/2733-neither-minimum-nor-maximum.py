class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)<=0:
            return -1
        nums.remove(max(nums))
        if len(nums)<=0:
            return -1
        nums.remove(min(nums))
        if len(nums)<=0:
            return -1
        return nums[-1]