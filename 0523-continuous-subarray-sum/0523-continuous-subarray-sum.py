class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s=0
        r={0:-1}
        for i,n in enumerate(nums):
            s+=n
            re=s%k
            if re not in r:
                r[re]=i
            elif abs(r[re]-i)>=2:
                return True
        return False