class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count=s.count('1')
        p=""
        count-=1
        for i in range(len(s)-1):
            if count>0:
                p+="1"
                count-=1
            else:
                p+="0"
        p+="1"
        return p