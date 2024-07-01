class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array
        
        closest_sum = float('inf')  # Initialize with a large number
        n = len(nums)
        
        for i in range(n - 2):  # Iterate until the third last element
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target  # Early return if exact match found
        
        return closest_sum
