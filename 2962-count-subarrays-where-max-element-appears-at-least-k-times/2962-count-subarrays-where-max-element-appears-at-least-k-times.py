from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def count_subarrays_with_max_at_least_k(max_val):
            count = 0
            window_start = 0
            max_count = 0
            
            for window_end in range(len(nums)):
                if nums[window_end] == max_val:
                    max_count += 1
                
                while max_count >= k:
                    count += len(nums) - window_end
                    if nums[window_start] == max_val:
                        max_count -= 1
                    window_start += 1
            
            return count
        
        max_count = 0
        max_val = max(nums)
        
        for num in nums:
            if num == max_val:
                max_count += 1
        
        if max_count < k:
            return 0
        
        return count_subarrays_with_max_at_least_k(max_val)
