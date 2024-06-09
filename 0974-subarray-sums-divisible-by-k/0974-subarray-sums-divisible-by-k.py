class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  
        running_sum = 0
        count = 0
        
        for num in nums:
            running_sum += num
            remain=running_sum%k
            count += prefix_sum[remain]
            prefix_sum[remain] += 1
            
        return count