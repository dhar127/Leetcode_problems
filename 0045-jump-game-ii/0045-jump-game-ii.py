class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps,end,start=0,0,0
        for i in range(len(nums)-1):
            start=max(start,i+nums[i])
            if i==end:
                jumps+=1
                end=start
        return jumps