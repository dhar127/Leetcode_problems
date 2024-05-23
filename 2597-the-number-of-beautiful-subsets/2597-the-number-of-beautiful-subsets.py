from collections import Counter
from functools import reduce
from operator import mul

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort() 
        count = 0

        def generate_subsets(start=0, subset=[]):
            nonlocal count
            if subset:  
                count += 1

            for i in range(start, n):
                subset.append(nums[i])
                if is_beautiful(subset, k):
                    generate_subsets(i + 1, subset)
                subset.pop()

        def is_beautiful(subset, k):
            last = subset[-1]
            for i in range(len(subset) - 1):
                if abs(subset[i] - last) == k:
                    return False
            return True

        generate_subsets()
        return count
