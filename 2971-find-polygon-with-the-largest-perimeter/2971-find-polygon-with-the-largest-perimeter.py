class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ts=0
        ans = -1
        
        for num in nums:
            if num < ts:
                ans = num + ts
            ts+= num
        
        return ans
        