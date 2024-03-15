class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=[1]*len(nums)
        start=1
        for i in range(len(nums)):
            r[i]*=start
            start*=nums[i]
        end=1
        for i in range(len(nums)-1,-1,-1):
            r[i]*=end
            end*=nums[i]
        return r
        