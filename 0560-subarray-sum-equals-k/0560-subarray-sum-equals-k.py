from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  
        running_sum = 0
        count = 0
        
        for num in nums:
            running_sum += num
           
            count += prefix_sum[running_sum - k]
          
            prefix_sum[running_sum] += 1
            
        return count
