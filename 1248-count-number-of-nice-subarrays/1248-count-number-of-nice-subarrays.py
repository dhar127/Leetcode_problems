class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        res = 0
        i = 0
        count = 0
        for ele in nums:
            if ele % 2 == 1:
                odd_count += 1
                count = 0

            while odd_count==k:
                if nums[i] % 2 == 1:
                    odd_count -= 1
                i += 1
                count += 1
                
            res += count
        return res