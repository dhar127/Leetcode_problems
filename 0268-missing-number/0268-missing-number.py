class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        f=0
        for i in range(len(nums)+1):
            f+=i
        return f-sum(nums)
        