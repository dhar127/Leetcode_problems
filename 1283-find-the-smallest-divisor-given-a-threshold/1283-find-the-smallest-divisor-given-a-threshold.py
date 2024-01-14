import math
class Solution:
   
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, 1000001
        while l < r:
            divisor = (r + l) // 2
            if sum(math.ceil(n / divisor) for n in nums) > threshold:
                l = divisor + 1
            else:       
                r = divisor
        return l