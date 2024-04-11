class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        j = 0
        for i in num:
            while len(s) > 0 and s[-1] > i and j < k:
                s.pop()
                j += 1
            s.append(i)
        while j < k and len(s) > 0:
            s.pop()
            j += 1
        res = ''.join(s).lstrip('0')
        return res if res else '0'
