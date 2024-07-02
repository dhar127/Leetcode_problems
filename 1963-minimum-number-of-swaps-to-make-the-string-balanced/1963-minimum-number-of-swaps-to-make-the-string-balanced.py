class Solution:
    def minSwaps(self, s: str) -> int:
        cnt=0
        l=[]
        for i in s:
            if i=="[":
                l.append('[')
            else:
                if l:
                    l.pop()
                else:
                    cnt+=1
                    l.append(']')
        return cnt