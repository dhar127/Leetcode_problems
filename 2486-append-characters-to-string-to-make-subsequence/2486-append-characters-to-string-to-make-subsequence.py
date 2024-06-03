class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        slen=len(s)
        tlen=len(t)
        i,j=0,0
        while i<slen and j<tlen:
            if s[i]==t[j]:
                j+=1
            i+=1
        return tlen-j