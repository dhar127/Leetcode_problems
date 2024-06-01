class Solution:
    def largestPalindromic(self, num: str) -> str:
        count=collections.defaultdict(int)
        for n in num:
            count[n]+=1
        res=''
        for i in '9876543210':
            res+=(count[i]//2*i)
        res=res.lstrip('0')
        mid=max(count[i]%2*i for i in count)
        return res+mid+res[::-1] or '0'
        