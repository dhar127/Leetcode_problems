class Solution:
    def removeDuplicates(self, s: str) -> str:
        g=[s[0]]
        for i in range(1,len(s)):
            if len(g)==0 or g[-1]!=s[i]:
                g.append(s[i])
            else:
                g=g[:-1]
        return "".join(g)