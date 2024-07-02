class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        min1 = nums[0]
        min2 = min(nums[1:])
        nums.remove(min1)
        nums.remove(min2)
        return min1 + min2 + min(nums)