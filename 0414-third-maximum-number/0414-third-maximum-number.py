class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if(len(nums))<=2:
            return max(nums)
        return sorted(nums)[-3]
        