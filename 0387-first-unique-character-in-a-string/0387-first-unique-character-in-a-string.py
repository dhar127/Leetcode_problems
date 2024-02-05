class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=[]
        for i in s:
            if s.count(i)==1:
                d.append(s.index(i))
        #print(d)
        return d[0] if len(d)!=0 else -1