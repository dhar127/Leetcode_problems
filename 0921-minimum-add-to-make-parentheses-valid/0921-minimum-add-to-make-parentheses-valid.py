class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l=[]
        g=0
        for i in s:
            if l:
                if l[-1]=='(' and i==')':
                    l.pop()
                else:
                    l.append(i)
            else:
                l.append(i)
        return len(l)