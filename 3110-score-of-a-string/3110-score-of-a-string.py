class Solution:
    def scoreOfString(self, s: str) -> int:
        x=0
        for i in range(len(s)-1):
            x+=abs(ord(s[i+1])-ord(s[i]))
        return x
            
        